insert into use_data (session_id,finger,pressure,hand) values
(1,'index',200,0),(1,'little',100,0),(1,'middle',50,0),(1,'ring',40,0),
(1,'index',175,0),(1,'little',22,0),(1,'middle',85,0),(1,'ring',8,0),
(1,'index',32,0),(1,'little',74,0),(1,'middle',102,0),(1,'ring',0,0),
(1,'index',0,1),(1,'little',50,1),(1,'middle',50,1),(1,'ring',136,1),
(1,'index',10,1),(1,'little',48,1),(1,'middle',50,1),(1,'ring',145,1),
(1,'index',85,1),(1,'little',200,1),(1,'middle',50,1),(1,'ring',78,1);


insert into session (patient_id,session_date) values
(1,date(2025-10-20));

insert into use_data (session_id,finger,pressure,hand) values
(2,'index',22,0),(2,'little',32,0),(2,'middle',175,0),(2,'ring',8,0),
(2,'index',175,0),(2,'little',22,0),(2,'middle',85,0),(2,'ring',8,0),
(2,'index',32,0),(2,'little',74,0),(2,'middle',8,0),(2,'ring',100,0),
(2,'index',22,1),(2,'little',120,1),(2,'middle',120,1),(2,'ring',136,1),
(2,'index',85,1),(2,'little',22,1),(2,'middle',89,1),(2,'ring',22,1),
(2,'index',175,1),(2,'little',200,1),(2,'middle',50,1),(2,'ring',78,1);