# 使用者認證

一般的應用程式會有認證機制，以便於了解使用者是誰?並且讓應用程式針對這個人有適當的回應

## Flask認證擴充程式

python有非常多好的認證擴充程式，但沒有一個可以做到所有的認證功能，所以必需整合部份的擴充程式，成為一套完整的認證機制。

- Flask-Login:管理使用者的登入和使用者的session
- Werkzeug:密碼的雜湊和驗證
- itsdangerous:加密和驗證

認證機制可以整合到以下的套件

- Flask-Mail:傳送一個驗證用的mail
- Flask-Bootstrap:HTML樣版
- Flask-WTF:網頁表單

## 使用Werkzeuge雜湊密碼

Werkzeuge的安全模組可以完成雜湊密碼的工作。雜湊密碼主要有分為2個階段，建立密碼雜湊和驗證密碼雜湊

雜湊密碼是無法回推成為原慶密碼

- 建立雜湊密碼

		generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
		
	這個function,將一般的密碼文字，透過method指定的運算機制，產生一個雜湊密碼，雜湊密碼將被儲存於資料庫內，使用method和salt_length參數的預設值就足夠應付大部份的需求
	
- 驗證雜湊密碼

		check_password_hash(hash, password)	

這個function, 將是從資料庫取出雜湊密碼並且比對使用者密碼，如果是正確的將會傳回True。


