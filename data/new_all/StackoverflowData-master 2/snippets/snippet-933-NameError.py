#Source: https://stackoverflow.com/questions/25491328/typeerror-when-creating-a-wtform-with-mongoengine-and-flask
app.logger.debug(isinstance(Post, mongoengine.base.BaseDocument))
app.logger.debug(isinstance(Post, mongoengine.base.DocumentMetaclass))