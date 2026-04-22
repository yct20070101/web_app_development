# 路由設計 (API & Route Design) - 個人記帳簿系統

## 1. 路由總覽表格

| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| --- | --- | --- | --- | --- |
| **首頁與設定 (Main)** | | | | |
| 月度收支總覽 | GET | `/` | `main/index.html` | 顯示當月總收支、結餘與近期紀錄 |
| 設定頁面 | GET | `/settings` | `main/settings.html` | 顯示預算與類別設定表單 |
| 更新預算 | POST | `/settings/budget` | — | 接收表單並更新預算，重導向至設定頁 |
| **記帳紀錄 (Records)** | | | | |
| 紀錄列表 | GET | `/records` | `records/index.html` | 顯示所有紀錄，支援搜尋與篩選 |
| 新增紀錄頁面 | GET | `/records/new` | `records/form.html` | 顯示新增表單 |
| 建立紀錄 | POST | `/records` | — | 接收表單並存入 DB，成功後重導向 |
| 編輯紀錄頁面 | GET | `/records/<id>/edit`| `records/form.html` | 顯示特定紀錄的編輯表單 |
| 更新紀錄 | POST | `/records/<id>/update`| — | 接收表單更新 DB，成功後重導向 |
| 刪除紀錄 | POST | `/records/<id>/delete`| — | 從 DB 刪除特定紀錄，重導向至列表 |
| **統計分析 (Analytics)**| | | | |
| 類別分類統計 | GET | `/analytics` | `analytics/index.html` | 顯示支出/收入比例統計圖表 |

## 2. 每個路由的詳細說明

### `GET /` (月度收支總覽)
- **輸入**: (無)
- **處理邏輯**: 呼叫 `Record.get_monthly_summary()` 取得當月統計，呼叫 `Setting.get_value('monthly_budget')` 取得預算。
- **輸出**: 渲染 `main/index.html`。

### `GET /settings` & `POST /settings/budget`
- **輸入**: POST 時接收 `budget` 表單欄位。
- **處理邏輯**: GET 時讀取現有預算；POST 時呼叫 `Setting.set_value()` 更新預算。
- **輸出**: POST 成功後重導向回 `/settings`，並帶有 Flash 訊息。

### `GET /records` (紀錄列表)
- **輸入**: URL 查詢參數如 `?year_month=2026-04&category_id=1`。
- **處理邏輯**: 呼叫 `Record.get_all(filters)` 獲取過濾後的紀錄。
- **輸出**: 渲染 `records/index.html`。

### `GET /records/new` & `POST /records`
- **輸入**: POST 時接收 `amount`, `date`, `category_id`, `description`。
- **處理邏輯**: GET 時提供分類清單 `Category.get_all()` 給下拉選單；POST 時呼叫 `Record.create()`，並檢查是否超過預算設定 Flash 訊息。
- **輸出**: 成功重導向至 `/records`，若驗證失敗重新渲染 `records/form.html`。

### `GET /records/<id>/edit` & `POST /records/<id>/update`
- **輸入**: URL 參數 `id`；POST 時接收更新的表單欄位。
- **處理邏輯**: 確認 `id` 存在，呼叫 `Record.update()`。
- **輸出**: 成功重導向至 `/records`，404 若找不到該紀錄。

### `POST /records/<id>/delete`
- **輸入**: URL 參數 `id`。
- **處理邏輯**: 呼叫 `Record.delete(id)`。
- **輸出**: 刪除後重導向至 `/records`。

### `GET /analytics`
- **輸入**: URL 查詢參數如 `?year_month=2026-04&type=expense`。
- **處理邏輯**: 彙整特定月份的分類花費總和。
- **輸出**: 渲染 `analytics/index.html` 並將資料傳給前端供圖表繪製。

## 3. Jinja2 模板清單
以下是預計建立的模板檔案結構：
- `base.html`：所有頁面共用的外層 HTML (包含 header, nav, footer, Flash 訊息顯示)。
- `main/index.html`：繼承 `base.html`，顯示 Dashboard。
- `main/settings.html`：繼承 `base.html`，顯示設定表單。
- `records/index.html`：繼承 `base.html`，顯示明細表格與搜尋介面。
- `records/form.html`：繼承 `base.html`，新增與編輯共用的表單介面。
- `analytics/index.html`：繼承 `base.html`，顯示圖表區域。
