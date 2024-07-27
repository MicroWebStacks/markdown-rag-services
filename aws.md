# S3 Policy
```json
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "Statement1",
			"Effect": "Allow",
			"Action": [
				"s3:GetObject",
				"s3:PutObject",
				"s3:DeleteObject"
			],
			"Resource": [
				"arn:aws:s3:::markdown-rag/*"
			]
		}
	]
}
```

# SNS Policy
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
            "sns:ListTagsForResource",
            "sns:Publish",
            "sns:GetTopicAttributes",
            "sns:Subscribe",
            "sns:ConfirmSubscription"
      ],
      "Resource": "arn:aws:sns:*"
    }
  ]
}
```
