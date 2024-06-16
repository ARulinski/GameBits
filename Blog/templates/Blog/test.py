    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['commentform'] = CommentForm()
        context['replyform'] = ReplyForm()
        return context

    def post(self, request, *args, **kwargs):
        article = self.get_object()
        commentform = CommentForm(request.POST)
        if not request.user.is_authenticated:
            return redirect('login_view')
        else:
            if commentform.is_valid():
                comment = commentform.save(commit=False)
                comment.article = article   
                comment.name = request.user
                comment.save()
                return redirect('article_view', pk=article.pk)  
            else:
                context = self.get_context_data(object=self.object)
                context['commentform'] = commentform
                return self.render_to_response(context)