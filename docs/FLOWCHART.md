# 流程圖設計 (Flowchart) - 個人記帳簿系統

## 1. 使用者流程圖 (User Flow)
描述使用者在系統中的主要操作路徑。

```mermaid
flowchart LR
    A([使用者開啟系統]) --> B[首頁 - 月度收支總覽]
    B --> C{選擇操作}
    
    C -->|點擊新增紀錄| D[新增紀錄表單]
    D -->|填寫金額、日期、類別並送出| E[儲存成功，返回總覽或清單]
    
    C -->|點擊查看明細/搜尋| F[記帳清單頁面]
    F --> G{針對特定紀錄}
    G -->|編輯| H[編輯紀錄表單]
    H -->|儲存| F
    G -->|刪除| I[確認刪除]
    I -->|是| F
    
    C -->|查看統計| J[類別分類統計圖表]
    
    C -->|設定| K[預算與類別設定]
```

## 2. 系統序列圖 (Sequence Diagram)
描述「使用者新增記帳紀錄」的完整系統互動流程。

```mermaid
sequenceDiagram
    actor User as 使用者
    participant Browser as 瀏覽器
    participant Route as Flask Route (records.py)
    participant Model as Model (record.py)
    participant DB as SQLite 資料庫
    
    User->>Browser: 在新增表單填寫收支資料並點擊送出
    Browser->>Route: POST /records/add (帶有表單資料)
    Route->>Route: 驗證資料格式 (金額、日期、類別)
    alt 資料無效
        Route-->>Browser: 回傳錯誤訊息，停留在表單頁
        Browser-->>User: 顯示提示 (例如：金額必須為數字)
    else 資料有效
        Route->>Model: 呼叫 create_record(data)
        Model->>DB: 執行 INSERT INTO records ...
        DB-->>Model: 新增成功
        Model-->>Route: 回傳成功狀態
        Route->>Route: 檢查是否超過本月預算
        alt 超過預算
            Route-->>Browser: 設定 Flash 訊息 (預算超支提醒)
        else 未超過
            Route-->>Browser: 設定 Flash 訊息 (新增成功)
        end
        Route-->>Browser: 重新導向 (302 Redirect) 至清單頁或首頁
        Browser-->>User: 顯示最新紀錄與提示訊息
    end
```

## 3. 功能清單對照表

| 功能描述 | URL 路徑 | HTTP 方法 | 負責的 Flask Route |
| --- | --- | --- | --- |
| 首頁 (月度收支總覽) | `/` | GET | `main.index` |
| 記帳清單 (含搜尋與篩選) | `/records` | GET | `records.list_records` |
| 顯示新增紀錄表單 | `/records/add` | GET | `records.add_record_form` |
| 處理新增紀錄請求 | `/records/add` | POST | `records.add_record` |
| 顯示編輯紀錄表單 | `/records/edit/<id>` | GET | `records.edit_record_form` |
| 處理編輯紀錄請求 | `/records/edit/<id>` | POST | `records.edit_record` |
| 處理刪除紀錄請求 | `/records/delete/<id>` | POST | `records.delete_record` |
| 類別分類統計頁面 | `/analytics` | GET | `analytics.show_stats` |
| 預算與類別設定 | `/settings` | GET | `main.settings` |
| 更新預算設定 | `/settings/budget` | POST | `main.update_budget` |
