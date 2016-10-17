from storages.backends.s3boto import S3BotoStorage

# Sets the static folder in S3
class StaticStorage(S3BotoStorage):
	location = "static"

# Sets the media folder in S3
class MediaStorage(S3BotoStorage):
	location = "media"