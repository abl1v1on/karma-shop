from wish_list.models import WishList


def check_item(user_id, product_id):
    return WishList.objects.filter(user_id=user_id, product_id=product_id).exists()


def add_item_in_wish_list(user_id, product_id):
    WishList.objects.create(user_id=user_id, product_id=product_id)


def remove_item_from_wish_list(user_id, product_id):
    WishList.objects.get(user_id=user_id, product_id=product_id).delete()
