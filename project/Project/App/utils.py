# from .models import Task, Post
# from Project.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME
# import boto3
# from boto3.session import Session
# from datetime import datetime

# def upload_and_save(request, file_to_upload):
#     session = Session(
#         aws_access_key_id = AWS_ACCESS_KEY_ID,
#         aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
#         region_name = AWS_S3_REGION_NAME
#     )
#     s3 = session.resource('s3')
#     now = datetime.now().strftime("%Y%H%M%S")

#     file_object = s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
#         Key = str(new_task.pk)+'/' + now + new_task.title,
#         Body = file_to_upload
#     )

#     s3_url = 'https://sanggyeong-bucket.s3.ap-northeast-2.amazonaws.com/'
    
#     post = Post.objects.create(
#         task = new_task,
#         author = new_task.author,
#         description = request.POST['description'],
#         img = s3_url+ str(new_task.pk)+'/'+ now+ new_task.title
#     )

