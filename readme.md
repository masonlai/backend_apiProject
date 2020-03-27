
#insert<br>
comment = Comment(content, page_id, creating_date, user_id)
db.session.add(comment)
<br>
db.session.commit()

#get first one record<br>
user = User.query.filter_by(User.username == '123').first()

#get all record<br>
videos = Video.query.filter(Video.comment_id == '123').all()
