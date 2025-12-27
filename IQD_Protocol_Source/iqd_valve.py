import json
import numpy as np
import os
import sys
from sentence_transformers import SentenceTransformer

# ==============================================================================
# 1. 語意向量引擎 (Semantic Vector Engine)
# ==============================================================================
class VectorEngine:
# 原本是 'all-MiniLM-L6-v2' (ABC 腦)
    # 改成下面這個 (翻譯官腦)
    def __init__(self, model_name='paraphrase-multilingual-MiniLM-L12-v2'):
        print(f">>> [System] Initializing Multilingual Neural Network ({model_name})...")
        self.model = SentenceTransformer(model_name)
    def get_embedding(self, text: str) -> np.ndarray:
        """將文字轉換為高維語意向量 (Normalized)"""
        vec = self.model.encode(text)
        return vec / np.linalg.norm(vec)

# ==============================================================================
# 2. IQD 協議核心 (IQD Protocol Core)
# ==============================================================================
class IQDProtocol:
    def __init__(self, manifest_path="iqd_core_manifest.json"):
        # 1. 載入 DNA
        try:
            with open(manifest_path, 'r', encoding='utf-8') as f:
                self.dna = json.load(f)
        except Exception as e:
            print(f"[Fatal Error] DNA 載入失敗: {e}")
            sys.exit(1)
            
        self.ve = VectorEngine()
        self.axes_pos = {}
        self.axes_neg = {}
        
        # 負向錨點定義
        self.neg_definitions = {
            "q5": "Loss of purpose, ethical corruption, chaotic entropy",
            "q4": "Illegal, violation of timing, chaos, anarchy",
            "q3": "Confused logic, panic, emotional instability",
            "q2": "Weak leadership, lack of agency, distrust, passive",
            "q1": "Bankruptcy, poverty, lack of resources, budget cut, no money",
            "q0": "Hardware failure, biological exhaustion, impossible to execute"
        }
        
        print(">>> [IQD] Calibrating Differential Logic Probes...")
        dims = self.dna['dimensions']
        
        for key in ["q0", "q1", "q2", "q3", "q4", "q5"]:
            # 優先抓 'pos_def'，如果沒有則抓 'vector_def'
            pos_text = dims[key].get('pos_def', dims[key].get('vector_def'))
            
            if not pos_text:
                print(f"[Warning] Key {key} missing definition!")
                continue

            # 正向向量
            self.axes_pos[key] = self.ve.get_embedding(pos_text)
            
            # 負向向量 (差分探針)
            neg_text = self.neg_definitions.get(key, "Lack of " + pos_text)
            self.axes_neg[key] = self.ve.get_embedding(neg_text)
            
            print(f"    • Probe {key} calibrated.")

    def measure_hexagram(self, user_prompt: str) -> str:
        """
        執行差分量子測量：Score = Sim(User, Pos) - Sim(User, Neg)
        """
        user_vec = self.ve.get_embedding(user_prompt)
        bits = []
        debug_log = []
        
        # 依序測量 q0 到 q5
        for key in ["q0", "q1", "q2", "q3", "q4", "q5"]:
            pos_vec = self.axes_pos[key]
            neg_vec = self.axes_neg[key]
            
            # 計算正負向相似度
            sim_pos = np.dot(user_vec, pos_vec)
            sim_neg = np.dot(user_vec, neg_vec)
            
            # === [核心物理公式] 差分判斷 ===
            diff = sim_pos - sim_neg
            
            # 設定 "中道閾值" (Hysteresis)
            bit = 1 if diff > 0.02 else 0
            bits.append(bit)
            
            dim_cn = self.dna['dimensions'][key]['name_cn']
            # debug 顯示差分值
            debug_log.append(f"{dim_cn}:{diff:+.2f}[{bit}]")

        # 反轉 bits 以符合 "上爻...初爻" 的 Key 格式 (例如 111111)
        hex_key = "".join(map(str, reversed(bits)))
        
        print(f"\n>>> [IQD Measurement Log] Input: '{user_prompt[:15]}...'")
        print("    " + " | ".join(debug_log))
        print(f"    -> Wavefunction Collapse: {hex_key}")
        
        return hex_key

    def ground(self, user_prompt: str):
        """
        [這是你之前缺少的函式] 接地主程式：執行邏輯判斷
        """
        hex_key = self.measure_hexagram(user_prompt)
        state = self.dna['states'].get(hex_key)
        
        if not state:
            return {
                "unicode": "???", 
                "name": "Unknown Chaos", 
                "physics": "Logic coherence failed.", 
                "audit": "System_Error"
            }
            
        return {
            "status": "GROUNDED",
            "hex": hex_key,
            "unicode": state['u'],
            "name": state['name'],
            "physics": state['vector'],
            "audit": state['audit']
        }

# ==============================================================================
# 3. 安全閥裝飾器 (Safety Valve Middleware)
# ==============================================================================
# 初始化全域協議
_iqd_instance = IQDProtocol()

def iqd_safety_valve(func):
    """
    Middleware: 攔截 Prompt -> 接地檢查 -> 注入物理限制
    """
    def wrapper(user_prompt, *args, **kwargs):
        # 1. 接地檢查 (呼叫剛剛補上的 ground 函式)
        result = _iqd_instance.ground(user_prompt)
        
        # 2. 顯示診斷面板
        print(f"\n[IQD SAFETY VALVE] Active.")
        print(f"   State: {result['unicode']} {result['name']}")
        print(f"   Audit: {result['audit']}")
        print(f"   Physics: {result['physics']}")
        
        # 3. 系統提示詞注入 (System Prompt Injection)
        injected_prompt = (
            f"[SYSTEM_PROTOCOL_OVERRIDE]\n"
            f"Logic Topology: {result['name']} ({result['audit']})\n"
            f"Physics Constraint: {result['physics']}\n"
            f"User Query: {user_prompt}\n"
            f"Mandate: Respond to the query while STRICTLY adhering to the Physics Constraint. "
            f"If resources are low, advise conservation. If risks are high, advise caution.\n"
        )
        
        # 4. 放行
        return func(injected_prompt, *args, **kwargs)
        
    return wrapper

# ==============================================================================
# 4. 應用層測試 (Application Layer)
# ==============================================================================

@iqd_safety_valve
def ai_inference_engine(prompt):
    """
    模擬對接 LLM 的接口
    """
    print("\n--- [LLM Inference Engine] ---")
    print(f"Processing Prompt:\n{prompt}")
    print("------------------------------")

if __name__ == "__main__":
    print("--- Test Case 1: Resource Scarcity ---")
    ai_inference_engine("我想建立一個強大的團隊來執行運算，但我完全沒有錢，預算被砍光了。")
    
    print("\n\n--- Test Case 2: Ideal State ---")
    ai_inference_engine("我們資金充足，團隊默契很好，法規也都通過了，準備開始執行。")