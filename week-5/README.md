# 要求三：SQL CRUD

## 使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。
### 指令： insert into member (name,username,password) values('test','test','test');

<img width="813" alt="2022-01-28_23-31-18" src="https://user-images.githubusercontent.com/23125379/151580959-3ee38dbb-5111-4cd5-a1dc-78e0cea3eded.png">

## 使用 SELECT 指令取得所有在 member 資料表中的會員資料。

<img width="815" alt="2022-01-28_23-32-30" src="https://user-images.githubusercontent.com/23125379/151581085-ce20a644-a49d-4bca-9d20-e240eb626ac7.png">

## 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。

<img width="815" alt="2022-01-28_23-35-43" src="https://user-images.githubusercontent.com/23125379/151581244-6bfcc242-6124-480f-80bd-349a1c04c6fd.png">

## 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )
<img width="815" alt="2022-01-28_23-42-25" src="https://user-images.githubusercontent.com/23125379/151581302-b102898a-db39-4c08-9284-d626e853de41.png">

## 使用 SELECT 指令取得欄位 username 是 test 的會員資料。

<img width="815" alt="2022-01-28_23-59-27" src="https://user-images.githubusercontent.com/23125379/151581465-aa9ee811-929e-4767-a7de-40a8800838f0.png">

## 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。

<img width="815" alt="2022-01-29_00-03-06" src="https://user-images.githubusercontent.com/23125379/151581580-b267af7a-75bc-4168-822a-fa0277f5bc28.png">

## 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。

<img width="815" alt="2022-01-29_00-11-03" src="https://user-images.githubusercontent.com/23125379/151581704-aa4e23d0-4d53-4d80-b25b-f7c29d367cd4.png">
