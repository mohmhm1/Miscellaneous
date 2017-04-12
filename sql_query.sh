#!/bin/sh

dbname="postgres://gqmqmsbthmqfxk:FwKpVbfkC6CqHMkeV4YDH8Fgso@ec2-107-20-148-211.compute-1.amazonaws.com:5432/d8co6a8128pa0i"
sudo psql $dbname << EOF
\Copy (SELECT * FROM services Where resolved = False) To 'test.csv' With CSV;
EOF
