
counter = 10000


def staff_info():
    global counter  
    
    date = input("Enter the date (MM/DD/YYYY): ")
    staff_id = input("Enter the Staff ID: ")
    staff_name = input("Enter the Staff Name: ")

    
    requisition_id = counter + 1  
   
    counter += 1
    
   
    return date, staff_id, staff_name, requisition_id



def requisition_approval(total_value, staff_id, requisition_id):
   
    status = "Pending"
    approval_reference = ""

    
    if total_value < 500:
        status = "Approved"
        
       
        approval_reference = f"{staff_id}{str(requisition_id)[-3:]}"
    
    
    print(f"\nTotal: ${total_value:.2f}")
    print(f"Status: {status}")
    if status == "Approved":
        print(f"Approval Reference Number: {approval_reference}")
    else:
        print("Approval Reference Number: N/A")



def requisitions_total():
    
    date, staff_id, staff_name, requisition_id = staff_info()
    
    
    total_value = 0
    
    while True:
        item_name = input("Enter the item name (or type 'done' to finish): ")
        
        if item_name.lower() == 'done':
            break
        
        try:
            item_price = float(input(f"Enter the price of {item_name}: $"))
        except ValueError:
            print("Invalid input for price. Please enter a valid number.")
            continue
        
        total_value += item_price

    
    return total_value, staff_id, requisition_id



def main():
    
    total_value, staff_id, requisition_id = requisitions_total()
    
    
    requisition_approval(total_value, staff_id, requisition_id)



main()
