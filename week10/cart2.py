from cart import Cart

if __name__ == "__main__":
    jim = Cart('Jim')
    jim.add_to_cart('waffle', 123, 3)
    print(jim.sub_total())