AI Voice Mimic — 聲音模仿系統
📢 說明（開頭最顯眼）
本專案為一個使用 AI 技術進行聲音模仿 的系統，可將使用者輸入的文字或聲音轉換為特定目標人物的聲音。此系統結合語音合成（TTS）、語音轉語音（Voice Conversion）技術與 LLM 提供語言處理輔助。

✅ 專案類型與製作說明
項目	說明
專案分類	🎧 AI 聲音應用 / TTS / 語音風格轉換
製作方式	原創設計 + 使用 AI 工具 + 參考開源資源，主要邏輯自行實作
查詢工具	使用 ChatGPT 查詢 CSS、音訊處理函式、Python TTS 函式庫用法

🧠 專案原理與技術
核心技術：
🗣️ Voice Conversion：模仿目標人物聲音（可使用 so-vits-svc 或 RVC）

🧾 Text-to-Speech (TTS)：gTTS、Tortoise TTS、Bark、ElevenLabs 等

🎧 Whisper：將聲音轉為文字（語音辨識）

🤖 LLM (如 Gemini)：語言理解與轉換（例如風格改寫）

🛠️ 系統架構與功能
後端（Python Flask）
語音辨識：Whisper 轉文字

語音模仿：so-vits-svc 或 RVC 進行聲音轉換

文字轉語音：Bark / ElevenLabs 模仿指定語音風格

LLM 輔助：語句優化（如「請幫我把這句話用古風說法說出來」）

前端:（HTML + JS + CSS）
語音上傳與播放

模仿角色選擇（Ex. 名人聲音、動漫角色）

輸入文字直接模仿語音

語音 vs 模仿聲音比對播放功能