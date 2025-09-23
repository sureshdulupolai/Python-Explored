from flask import Blueprint, render_template, request, redirect, flash, url_for, send_from_directory
import requests

product_bp = Blueprint("product_bp", __name__)
API_URL = "http://127.0.0.1:8000"

# Path to FastAPI media folder
MEDIA_DIR = r"C:\Users\user\Desktop\suresh\Python_Lib\Python\new_api\Backend\media"

# Serve media files in Flask
@product_bp.route('/media/<filename>')
def media(filename):
    return send_from_directory(MEDIA_DIR, filename)

# List Products (GET: show all, POST: filtered)
@product_bp.route("/", methods=["GET", "POST"])
def list_products():
    search_query = ""
    category_filter = ""
    
    # Fetch categories for dropdown
    try:
        cat_res = requests.get(f"{API_URL}/categories/")
        categories = cat_res.json()
    except Exception as e:
        categories = []
        print("Error fetching categories:", e)

    params = {}
    if request.method == "POST":
        # Get filter data from form
        search_query = request.form.get("search", "")
        category_filter = request.form.get("category", "")
        if search_query:
            params["search"] = search_query
        if category_filter:
            params["category_id"] = category_filter

    # Fetch products from FastAPI
    try:
        res = requests.get(f"{API_URL}/products/", params=params)
        print("Params: ", params["category_id"], "Res Data: ", res)
        products = res.json()
    except Exception as e:
        products = []
        print("Error fetching products:", e)

    # Fix media URLs
    for p in products:
        if p.get("image") and not p["image"].startswith("http"):
            filename = p["image"].split("/")[-1]
            p["image"] = url_for("product_bp.media", filename=filename)

    return render_template(
        "products.html",
        products=products,
        categories=categories,
        search_query=search_query,
        category_filter=int(category_filter) if category_filter else ""
    )


# Add Product
@product_bp.route("/add", methods=["GET", "POST"])
def add_product():
    try:
        cat_res = requests.get(f"{API_URL}/categories/")
        categories = cat_res.json()
    except Exception as e:
        categories = []
        print("Error fetching categories:", e)

    if request.method == "POST":
        name = request.form.get("name")
        desc = request.form.get("desc")
        price = request.form.get("price")
        status = request.form.get("status")
        category_id = request.form.get("category")
        image_file = request.files.get("image")

        if not image_file:
            flash("Please upload an image", "danger")
            return redirect(url_for("product_bp.add_product"))

        data = {
            "name": name,
            "desc": desc,
            "price": price,
            "status": status,
            "category_id": category_id
        }
        files = {"image": (image_file.filename, image_file.read(), image_file.content_type)}

        try:
            res = requests.post(f"{API_URL}/products/", data=data, files=files)
            if res.status_code in (200, 201):
                flash("Product added successfully!", "success")
                return redirect(url_for("product_bp.list_products"))
            else:
                flash(f"Failed to add product: {res.text}", "danger")
        except Exception as e:
            print("Error adding product:", e)
            flash("Error adding product", "danger")

    return render_template("add_product.html", categories=categories)
