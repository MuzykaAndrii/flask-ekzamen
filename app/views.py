from flask import render_template, url_for, redirect, request, flash, abort
from app import app
from app.forms import ArticleForm
from app.models import Article
from . import db

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', name = 'Software engeneering', title = 'PNU')


@app.route('/article/new', methods=['GET', 'POST'])
def new_article():
    form = ArticleForm()

    if form.validate_on_submit():
        name = form.name.data
        note = form.note.data
        author = form.author.data
        year_posted = form.year_posted.data
        count_of_pages = form.count_of_pages.data
        type_of_art = form.type_of_art.data

        article = Article(name, year_posted, count_of_pages, author, note, type_of_art)
        article.save()

        flash('Article created successfully', 'success')
        return redirect(url_for('article', article_id=article.id))

    return render_template('create_article.html', title='Create new article', form=form, action='Create new article')

@app.route("/article/<int:article_id>")
def article(article_id):
    article = Article.query.get_or_404(article_id)
    return render_template('article.html', title=article.name, article=article)


@app.route('/articles', methods=['GET'])
def articles():
    # Set the pagination configuration
    POSTS_PER_PAGE = 5
    page = request.args.get('page', 1, type=int)
    search_query = request.args.get('search_query')

    if search_query:
        # paginate according to search query
        articles = Article.query.filter(Article.name.contains(search_query) | Article.content.contains(search_query)).paginate(page=page, per_page=POSTS_PER_PAGE)
    else:
        #paginate simply
        articles = Article.query.order_by(Article.year_posted.desc()).paginate(page=page, per_page=POSTS_PER_PAGE)

    return render_template('articles.html', title='Articles', articles=articles)

@app.route('/article/<int:article_id>/delete')
def delete_article(article_id):
    article = Article.query.get_or_404(article_id)
    article.delete()

    flash('Your article hes been deleted!', 'success')

    return redirect(url_for('articles'))

@app.route('/article/<int:article_id>/update', methods=['GET', 'POST'])
def update_article(article_id):
    article = Article.query.get_or_404(article_id)

    form = ArticleForm()

    if form.validate_on_submit():
        article.name = form.data.name
        article.note = form.data.note
        article.year_posted = form.data.year_posted
        article.count_of_pages = form.data.count_of_pages
        article.author = form.data.author
        article.type_of_art = form.data.type_of_art
        article.save()

        flash('Article updated succsesfully')
    
    elif request.method == 'GET':
        form.name.data = article.name
        form.note.data = article.note
        form.year_posted.data = article.year_posted
        form.count_of_pages.data = article.count_of_pages
        form.author.data = article.author
        form.type_of_art.data = article.type_of_art
    
    return render_template('create_article.html', title='Edit article', form=form, action='Edit article')


# @app.route('/article/new', methods=['GET', 'article'])
# def new_post():
#     form = CreatePostForm()

#     if form.validate_on_submit():
#         title = form.title.data
#         content = form.content.data
#         creator_id = current_user.id

#         article = article(title, content, creator_id)
#         article.save()

#         flash('article created successfully', 'success')
#         return redirect(url_for('article', post_id=article.id))

#     return render_template('create_post.html', title='Create new article', form=form, action='Create new article')



# @app.route('/article/<int:post_id>/update')
# def update_post(post_id):
#     article = article.query.get_or_404(post_id)
#     if article.user_id != current_user.id:
#         abort(403)

#     form = CreatePostForm()

#     if form.validate_on_submit():
#         article.title = form.data.title
#         article.content = form.data.content
#         article.date_posted = dt.now()
#         article.save()
    
#     elif request.method == 'GET':
#         form.title.data = article.title
#         form.content.data = article.content
    
#     return render_template('create_post.html', title='Edit article', form=form, action='Edit article')

# @app.route('/article/<int:post_id>/delete')
# def delete_post(post_id):
#     article = article.query.get_or_404(post_id)
#     if article.user_id != current_user.id:
#         abort(403)
#     article.delete()
#     flash('Your article hes been deleted!', 'success')
#     return redirect(url_for('posts'))
