from core.renderers import CoreJSONRenderer


class ArticleJSONRenderer(CoreJSONRenderer):
    object_label = 'article'
    pagination_object_label = 'articles'
    pagination_count_label = 'articlesCount'


class CommentJSONRenderer(CoreJSONRenderer):
    object_label = 'comment'
    pagination_object_label = 'comments'
    pagination_count_label = 'commentsCount'
