# creates a file in /tmp

File { '/tmp/school':
	Content => 'I love Puppet' ,
	mode => '0744' ,
	owner => 'www-data' ,
	group => 'www-data' ,
}