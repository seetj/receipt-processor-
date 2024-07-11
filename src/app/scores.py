from datetime import datetime,time
import math

def score_retailer_name(receipt):
    score = 0 
    retailer_name = [char for char in receipt.retailer]
    for char in retailer_name:
        if char.isalnum() == True:
            score += 1 
    return score 

def score_receipt_length(receipt):
    score = 0
    score  += (len(receipt.items)//2 ) * 5
    return score 

def score_price_end_with_00(receipt):
    score = 0 
    if receipt.total.endswith(".00") == True:
        score += 50
    return score 

def score_price_multiple_of_25(receipt):
    score = 0 
    if float(receipt.total) % 0.25 == 0:
        score += 25
    return score

def score_item_description_length(receipt):
    score = 0
    for item in receipt.items:
        if len(item.shortDescription.strip()) % 3 == 0:
            score += math.ceil(float(item.price) * 0.2)
    return score    

def score_purchase_date_odd(receipt):
    score = 0 
    date = datetime.strptime(receipt.purchaseDate, "%Y-%m-%d").date()
    if date.day % 2 != 0:
        score += 6
    return score 

def score_purchase_between_2pm_and_4pm(receipt):
    score = 0
    purchase_time = receipt.purchaseTime
    start_time = time(14, 0) 
    end_time = time(16, 0)  

    if start_time < purchase_time < end_time:
        score += 10
    return score 

def total_score(receipt):
    total_score = 0
    
    total_score += score_retailer_name(receipt)
    total_score += score_receipt_length(receipt)
    total_score += score_price_multiple_of_25(receipt)
    total_score += score_price_end_with_00(receipt)
    total_score += score_item_description_length(receipt)
    total_score += score_purchase_between_2pm_and_4pm(receipt)
    total_score += score_purchase_date_odd(receipt)

    return total_score
    
