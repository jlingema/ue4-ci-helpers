import boto3

class AWSUtils(object):
	'''
	Provides functionality related to Amazon Web Services (AWS)
	'''
	
	# Amazon EC2 utilities
	
	@staticmethod
	def is_instance_running(id):
		'''
		Determines if the specified Amazon EC2 instance is currently running.
		
		`id` is the ID of the EC2 instance to be queried.
		'''
		ec2 = boto3.resource('ec2')
		return ec2.Instance(id).state['Name'] == 'running'
	
	@staticmethod
	def start_instance(id):
		'''
		Starts an Amazon EC2 instance if it is not already running.
		
		`id` is the ID of the EC2 instance to be started.
		'''
		
		# Retrieve the instance handle
		ec2 = boto3.resource('ec2')
		instance = ec2.Instance(id)
		
		# If the instance is currently stopping, wait for the stop to complete
		if instance.state['Name'] in ['shutting-down', 'stopping']:
			instance.wait_until_stopped()
		
		# Attempt to start the instance
		instance.start()
		instance.wait_until_running()
	
	@staticmethod
	def get_instance_ip(id):
		'''
		Retrieves the public IP address (if any) of an Amazon EC2 instance.
		
		`id` is the ID of the EC2 instance to be queried.
		'''
		ec2 = boto3.resource('ec2')
		return ec2.Instance(id).public_ip_address
	
	
	# Amazon S3 utilities
	
	@staticmethod
	def download_file(bucket, key, filename):
		'''
		Downloads a file from Amazon S3.
		
		`bucket` is the S3 Bucket name to download from.
		`key` is the key for the data that will be downloaded.
		`filename` is the path to the file that will receive the downloaded data.
		'''
		s3 = boto3.resource('s3')
		s3.Bucket(bucket).download_file(key, filename)
	
	@staticmethod
	def upload_file(bucket, key, filename):
		'''
		Uploads a file to Amazon S3.
		
		`bucket` is the S3 Bucket name to upload to.
		`key` is the key to assign to the uploaded data.
		`filename` is the path to the file containing the data that will be uploaded.
		'''
		s3 = boto3.resource('s3')
		s3.Bucket(bucket).upload_file(filename, key)
