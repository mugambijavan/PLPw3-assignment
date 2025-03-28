def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    :param price: Original price of the item
    :param discount_percent: Discount percentage to be applied
    :return: Final price after applying the discount or original price if discount is less than 20%
    """
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price

def main():
    # Prompt the user to enter the original price of an item
    price = float(input("Enter the original price of the item: "))
    
    # Prompt the user to enter the discount percentage
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate the final price using the calculate_discount function
    final_price = calculate_discount(price, discount_percent)
    
    # Print the final price or original price based on the discount
    if final_price != price:
        print(f"The final price after applying the discount is: {final_price}")
    else:
        print(f"No discount applied. The original price is: {price}")

if __name__ == "__main__":
    main()