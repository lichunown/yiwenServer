[TOC]

## 用户文章保存与读取

*测试服务器http://lcyown.cn:3000*

以`POST`形式传输信息



| 网址                      | 类别     |      |
| ----------------------- | ------ | ---- |
| /passage/getpassage     | 获取文章   |      |
| /passage/getpassagelist | 获取文章列表 |      |
| /passage/savepassage    | 保存文章   |      |
| /passage/changepassage  | 修改文章   |      |

### 获取文章列表

POST `/passage/getpassage`

**无需传入数据，只要是POST方法请求即可得到数据返回结果。**

#### 返回数据
```python
  {
            'action':'getpassagelist',
            'result':'succeed',
            'lists':[
              	{
                  'title':'title1',
                  'author':'author',
                  'time':'time1',
                  'id':'1'
              	},
              	{
                  'title':'title2',
                  'author':'author',
                  'time':'time2',
                  'id':'2'
              	}
            ]
   }
```

### 获取文章

POST `/passage/getpassage`

|  -   | key  | example |   info    |
| :--: | :--: | :-----: | :-------: |
|  *   |  id  |   "1"   | passage编号 |



#### 成功返回
```python
{
    {
    'action':'getpassage',
    'result':'succeed',
    'passage':{
        'id':'1',
        'title':'Passage Title',
        'author':'author',
        'body':'this is passage\'s body. ',
        'time':'POST passage time',
    },
}
```
#### 文章无法找到返回
```python
{
    'action':'getpassage',
    'result':'error',
    'errorResult':'PassageNotFound',
}
```

### 保存文章

POST `/passage/savepassage`

|  -   |  key  |     example     |    info    |
| :--: | :---: | :-------------: | :--------: |
|  *   | token |       "1"       | 用户登录的token |
|  *   | title | "Passage Title" |    文章标题    |
|  *   | body  | "lalalalalala。" |    文章内容    |

#### 保存成功返回
```python
{
      'action':'savepassage',
      'result':'succeed',
      'id':newPassage.id,
}
```
#### 用户匹配错误返回
```python
{
        'action':'savepassage',
        'result':'error',
        'errorResult':'TokenDoNotMatch',
}
```

### 修改文章
POST `/passage/changepassage`

|  -   |  key  |     example     |    info    |
| :--: | :---: | :-------------: | :--------: |
|  *   | token |       "1"       | 用户登录的token |
|  *   |  id   |       "1"       |    文章标号    |
|  *   | title | "Passage Title" |    文章标题    |
|  *   | body  | "lalalalalala。" |    文章内容    |

#### 成功返回
```python
{
        'action':'changepassage',
        'result':'succeed',
        'id':passageid,
}
```
#### 错误返回
##### 文章标号错误
```python
{
        'action':'changepassage',
        'result':'error',
        'errorResult':'PassageDoNotExists',
        'id':passageid,
}
```
##### 用户不匹配错误
修改用户必须是发表文章的用户，如果不符合，将报错。
```python
{
        'action':'changepassage',
        'result':'error',
        'errorResult':'PermissionDenied',
        'id':passageid,
}
```
##### 用户登录错误
```python
{
        'action':'savepassage',
        'result':'error',
        'errorResult':'TokenDoNotMatch',
}
```