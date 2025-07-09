import numpy as np
import pandas as pd

user = {
    'id' : [1, 2, 3, 4, 5],
    'username' : ['suresh', 'krish', 'pritam', 'akash', 'kalim'],
    'gmail' : ['suresh@gmail.com', 'krish@gmail.com', 'pritam@gmail.com', 'akash@gmail.com', 'kalim@gmail.com'],
    'pass' : ['suresh123', 'krish123', 'pritam123', 'akash123', 'kalim123']
}

profile = {
    'id' : [1, 2, 3, 4, 5],
    'id_user' : [1, 2, 3, 4, 5],
    'barCode' : ['dev123', 'cus123', 'cus124', 'dev124', 'cus125'],
    'category' : ['Developer', 'Customer', 'Customer', 'Developer', 'Customer'],
    'total_reciept' : [0, 1000, 0, 500, 0],
    'total_count' : [0, 3, 0, 1, 0],
    'mobile' : [1234567890] * 5
}

company = {
    'id' : [1, 2, 3, 4, 5, 6],
    'id_profile' : [2, 4, 2, 101, 102, 2],
    'payment' : ['Online', 'Cash', 'Cash', 'Online', 'Cash', 'Online'],
    'work' : ['Wash', 'Coting', 'Wash', 'Cotaing', 'Wash', 'Wash'],
    'recipt_no' : ['rec123', 'rec124', 'rec125', 'rec126', 'rec127', 'rec128']
}

order = {
    'id' : [1, 2],
    'id_user' : [1, 4],
    'work' : ['ppf', 'wash'],
    'payment_should' : [95000, 300],
    'status' : ['not seen', 'not seen']
}