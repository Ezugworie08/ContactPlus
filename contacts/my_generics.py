__author__ = 'Ikechukwu'
from rest_framework import mixins
from rest_framework import generics


class CreateDeleteAPIView(mixins.CreateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    """
    My own combination.
    Chris, I don't fully understand all the magic here.
    I am sure I can explain it away to some extent.
    """

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ListUpdateDeleteAPIView(mixins.ListModelMixin, mixins.UpdateModelMixin,
                              mixins.DestroyModelMixin,generics.GenericAPIView):

    """
    I see the pattern here but my understanding hasn't become second nature
    """

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
