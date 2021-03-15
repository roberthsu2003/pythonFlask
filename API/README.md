# Application Programming Interface

在最近這些年來，網站應用程式不再只是只有顯示內容，提供表單，網站應用功能也越來越多是注重使用者端的瀏覽器的功能，比方說使用javascript程式語言框架如Jquery,Vue,React,Angular.

當網站應用朝向使用都端的程式發展時，網站所提供的就是內容，由使用者端向網站提供提出需求，而網站就是提供內容或圖片或影片資料給使用者，網站所扮演的角色就成為儲存資料提供給使用者端的應用程式使用，這樣的模式稱為Web Service或者稱為application Programming Interface(API) 

使用者端和網站之間的溝通就非常重要，目前的主流的架構就是使用REST(Representational State Transfer)。

這個章節最主要說明，如何讓Flask提供RESTful API


## Request Methods
### RESTful API的HTTP request 方法

| Request Method | 溝通方式 | 說明 | HTTP response 狀態碼 |
|:--|:--|:--|:--|
| GET | URL | 取得一筆獨立資料 | 200 |
| GET | URL | 取得多頁資料(server要有分頁功能) | 200 |
| POST | URL | 建立一筆或多筆資料 | 201 |
| PUT | URL | 修改資料 | 200 或者 204|
| DELETE | URL | 刪除一筆資料 | 200 或者 204 |
| DELETE | URL | 刪除一筆資料 | 200 或者 204 |

> RESTful架構並不需要提供所有功能
