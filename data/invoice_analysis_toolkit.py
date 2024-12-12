import json


# 1) File Handling and JSON Processing
def load_invoices(filename):
    """
    Load invoices from a JSON file
    
    Args:
        filename (str): Path to the JSON file
    
    Returns:
        list: List of validated invoice dictionaries
    """
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Load JSON data from the file
            invoices = json.load(filename)
        
        # Validate invoices using a list comprehension
        validated_invoices = [
            invoice for invoice in invoices
            # Check that each invoice has required keys, all() ensures every specified key exists
            if all(key in invoice for key in ['invoice_id', 'customer_name', 'total_amount'])
        ]
        
        return validated_invoices
    
    except FileNotFoundError:
        # Handle case where the file doesn't exist
        print(f"Error: File {filename} not found")
        return []
    except json.JSONDecodeError:
        # Handle invalid JSON formatting
        print("Invalid JSON format")
        return []


# 2) Higher-Order Functions Exercise
def process_invoices(invoices):
    """
    Demonstrate higher-order function techniques
    
    Args:
        invoices (list): List of invoice dictionaries
    
    Returns:
        dict: Processed invoice information
    """
    # Filter paid invoices
    paid_invoices = list(filter(lambda invoice: invoice['payment_status'] == 'Paid', invoices))
    
    # Calculate total items per invoice
    total_items = list(map(
        lambda invoice: sum(item['quantity'] for item in invoice['items']), invoices
    ))
    
    return {
        'paid_invoices': paid_invoices,
        'total_items_per_invoice': total_items
    }


# 3) Comprehensions Exercise
def invoice_comprehensions(invoices):
    """
    Apply list and dictionary comprehensions
    
    Args:
        invoices (list): List of invoice dictionaries
    
    Returns:
        dict: Comprehension results
    """
    # List of customer names
    customer_names = [invoice['customer_name'] for invoice in invoices]
    
    # Dictionary of invoice totals by customer
    customer_totals = {
        invoice['customer_name']: invoice['total_amount'] for invoice in invoices
    }
    
    # High-value invoice details
    high_value_invoices = [
        {
            'customer': invoice['customer_name'],
            'total': invoice['total_amount']
        } for invoice in invoices if invoice['total_amount'] > 4000
    ]
    
    return {
        'customer_names': customer_names,
        'customer_totals': customer_totals,
        'high_value_invoices': high_value_invoices
    }


# 4) Mini-Project: Invoice Analytics



