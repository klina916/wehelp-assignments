
    // XMLHTTpRequest 物件專門用來和伺服器做連線
    let req= new XMLHttpRequest(); 

    let n = 0;
    req.open("get", "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json");
    req.responseType = 'json';
    req.onload = function generateImage(){  // load事件，偵測連線的狀態結束
        if(req.status == 200){  // 伺服器請求成功
            let box = document.querySelector('.bob-row');
          
            for (let i= 0+n; i < (8 + n); i++){  //圖片從第0筆開始，一次八張

                // API路徑
                let uriPath = req.response['result']['results'][i];

                let subTitle = uriPath['stitle'];

                // 將圖片字串用 split 函式從 "https://" 切開, 返回前兩筆結果, 第一筆在 https:// 之前為空白, 取第二個結果
                let imgUrl = 'https://' + uriPath['file'].split("https://", 2)[1]

                // 建立 div 元素, class name 為 bob-4item
                let content = document.createElement('div');
                content.className = 'bob-4item';

                // 我是圖片本人
                // 建立 img 元素, class name 為 object-fit
                let img = document.createElement('img'); 	
                img.className =  'object-fit'
                img.src = imgUrl; 
                console.log(img);

                // 我是圖片標題
                // 建立 div 元素, class name 為 title
                let imgTitle = document.createElement('div')
                imgTitle.className = 'title'
                imgTitle.textContent = subTitle;
                console.log(imgTitle);

                content.appendChild(img);
                content.appendChild(imgTitle);
                box.appendChild(content)

              }

            n += 8;

          } else{
              // 伺服器傳回了其他錯誤代碼
              console.log('Error');  
          }
        }

    req.send();  // 送出連線
