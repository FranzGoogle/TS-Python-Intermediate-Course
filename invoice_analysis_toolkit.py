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
            invoices = json.load(file)
        
        # Validate invoices using a list comprehension
        validated_invoices = [
            inv for inv in invoices
            # Check that each invoice has required keys, all() ensures every specified key exists
            if all(key in inv for key in ['invoice_id', 'customer_name', 'total_amount'])
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
    paid_invoices = list(filter(lambda inv: inv['payment_status'] == 'Paid', invoices))
    
    # Calculate total items per invoice
    total_items = list(map(
        lambda inv: sum(item['quantity'] for item in inv['items']), invoices
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
    customer_names = [inv['customer_name'] for inv in invoices]
    
    # Dictionary of invoice totals by customer
    customer_totals = {
        inv['customer_name']: inv['total_amount'] for inv in invoices
    }
    
    # High-value invoice details
    high_value_invoices = [
        {
            'customer': inv['customer_name'],
            'total': inv['total_amount']
        } for inv in invoices if inv['total_amount'] > 4000
    ]
    
    return {
        'customer_names': customer_names,
        'customer_totals': customer_totals,
        'high_value_invoices': high_value_invoices
    }


# 4) Mini-Project: Invoice Analytics
class InvoiceAnalyzer:
    def __init__(self, invoices):
        self.invoices = invoices
    
    def total_revenue(self):
        """Calculate total revenue"""
        return sum(inv['total_amount'] for inv in self.invoices)
    
    def revenue_by_status(self):
        """Group revenue by payment status"""
        status_revenue = {}
        for inv in self.invoices:
            status = inv['payment_status']
            status_revenue[status] = status_revenue.get(status, 0) + inv['total_amount']
        return status_revenue


### LAB CHALLENGE ###
def main():
    # Load invoices
    invoices = load_invoices('./data/invoice-data.json')
    
    # Process invoices
    processed_data = process_invoices(invoices)
    
    # Apply comprehensions
    comprehension_results = invoice_comprehensions(invoices)
    
    # Analyze invoices
    analyzer = InvoiceAnalyzer(invoices)
    
    # Print results
    print("Total Revenue:", analyzer.total_revenue())
    print("Revenue by Status:", analyzer.revenue_by_status())
    print("High-Value Invoices:", comprehension_results['high_value_invoices'])

if __name__ == "__main__":
    main()


