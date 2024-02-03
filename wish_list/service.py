class WishListService:
    def __init__(self, session, request):
        self.session = session
        self.request = request

    def add(self, pk):
        if self.request.method == 'POST':  # Проверяем запрос на метод POST
            if not self.request.session.get('wish_list'):  # Проверяем, есть ли в нашей сессии ключ wish_list
                print("NOT")
                self.request.session['wish_list'] = list()  # Если его нет, то создается пустой список
            else:  # Если он (ключ) есть, то мы создаем список с предыдущими значениями
                print("YES")
                self.session = list(self.session)

            # Проверяем, есть ли товар, который мы пытаемся добавить в нашем wish_list
            item_exists = next((i for i in self.session if i['id'] == pk), False)
            print(item_exists)
            # Принимаем данные нашего запроса
            app_data = {
                'id': pk
            }

            # Если товара, который мы пытаемся добавить в wish_list нет, то мы добавляем его
            if not item_exists:
                self.request.session['wish_list'].append(app_data)
                self.request.session.modified = True  # Указываем, что сессия была изменена

    def remove(self, pk):
        if self.request.method == 'POST':
            for i in self.session:  # Пробегаемся по нашему списку из добавленный товаров
                if i['id'] == pk:  # Если находим этот товар, то удаляем его
                    i.clear()

            # На месте удаленных товаров остается {}, поэтому их тоже нужно удалить
            while {} in self.session:
                self.session.remove({})

            # Тут мы проверяем, есть ли вообще у нас ключ wish_list в сессиях
            if not self.session:
                del self.session

            self.request.session.modified = True
