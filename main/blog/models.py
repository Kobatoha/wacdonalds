from django.db import models


class Post(models.Model):
    '''данные о записи: названия полей в таблице Post'''
    title = models.CharField('Заголовок записи', max_length=100)
    description = models.TextField('Текст записи')
    author = models.CharField('Имя автора', max_length=100)
    date = models.DateTimeField('Дата публикации')
    image = models.ImageField('Изображение', upload_to='image/%Y')

    def __str__(self):
        ''' отображение названий и авторов в превью таблицы '''
        return f'{self.title}, {self.date}'

    class Meta:
        ''' корректное отображение записей в единственном и множественном числе '''
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class Comments(models.Model):
    ''' комментарии от пользователей
        т.к. конкретный комментарий оставляется под конкретной записью,
        мы должны связать таблицу с комментариями и таблицу с записями;
        ForeignKey - ключ, по которому связываются две таблицы,
        связывается с таблицей (Post);
        on_delete - настройки поведения при удалении объекта - когда объект,
        на котороый имеется ссылка, удаляется, то так же удаляются все объекты, которые ссылаются на нее '''
    name = models.CharField('Имя', max_length=16)
    text_comments = models.TextField('Текст комментария', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)

    def __str__(self):
        ''' отображение названий и авторов в превью таблицы '''
        return f'{self.name}, {self.post}'

    class Meta:
        ''' корректное отображение записей в единственном и множественном числе '''
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Likes(models.Model):
    ''' модель фиксирования лайков и дизлайков к конкретному посту от уникального пользователя
        уникальность пользователя определеяется по ip-адресу из-за отсутствия регистрации/аутентификации'''
    ip = models.CharField('IP-адрес', max_length=200)
    pos = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)

