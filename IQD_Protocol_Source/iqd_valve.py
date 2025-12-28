import json
import numpy as np
import os
import sys
from sentence_transformers import SentenceTransformer

# ==============================================================================
# 1. Semantic Vector Engine
# ==============================================================================
class VectorEngine:
    """
    Handles text-to-vector encoding using multilingual transformer models.
    """
    def __init__(self, model_name='paraphrase-multilingual-MiniLM-L12-v2'):
        print(f">>> [System] Initializing Multilingual Neural Network ({model_name})...")
        self.model = SentenceTransformer(model_name)

    def get_embedding(self, text: str) -> np.ndarray:
        """Converts text into a normalized high-dimensional semantic vector."""
        vec = self.model.encode(text)
        return vec / np.linalg.norm(vec)

# ==============================================================================
# 2. IQD Protocol Core
# ==============================================================================
class IQDProtocol:
    def __init__(self, manifest_path="iqd_core_manifest.json"):
        # Load Protocol Manifest (The "DNA" of logical states)
        try:
            with open(manifest_path, 'r', encoding='utf-8') as f:
                self.dna = json.load(f)
        except Exception as e:
            print(f"[Fatal Error] Failed to load IQD Manifest: {e}")
            sys.exit(1)
            
        self.ve = VectorEngine()
        self.axes_pos = {}
        self.axes_neg = {}
        
        # Negative Anchor Definitions (The "Grounding" Reference)
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
            pos_text = dims[key].get('pos_def', dims[key].get('vector_def'))
            if not pos_text:
                continue

            # Positive Reference Vector
            self.axes_pos[key] = self.ve.get_embedding(pos_text)
            
            # Negative Reference Vector (Differential Probe)
            neg_text = self.neg_definitions.get(key, "Lack of " + pos_text)
            self.axes_neg[key] = self.ve.get_embedding(neg_text)
            print(f"    • Probe {key} calibrated.")

    def measure_hexagram(self, user_prompt: str) -> str:
        """
        Performs Differential Quantum Measurement: 
        Score = Sim(User, Pos) - Sim(User, Neg)
        """
        user_vec = self.ve.get_embedding(user_prompt)
        bits = []
        debug_log = []
        
        for key in ["q0", "q1", "q2", "q3", "q4", "q5"]:
            pos_vec = self.axes_pos[key]
            neg_vec = self.axes_neg[key]
            
            # Calculate Cosine Similarity for both polarities
            sim_pos = np.dot(user_vec, pos_vec)
            sim_neg = np.dot(user_vec, neg_vec)
            
            # [Core Physics Formula] Differential Logic Determination
            diff = sim_pos - sim_neg
            
            # Hysteresis Threshold (Bias Adjustment)
            bit = 1 if diff > 0.02 else 0
            bits.append(bit)
            
            dim_name = self.dna['dimensions'][key]['name_cn']
            debug_log.append(f"{dim_name}:{diff:+.2f}[{bit}]")

        # Map to Hexagram Key (Reversed for correct bit order)
        hex_key = "".join(map(str, reversed(bits)))
        
        print(f"\n>>> [IQD Measurement Log] Input: '{user_prompt[:20]}...'")
        print("    " + " | ".join(debug_log))
        print(f"    -> Wavefunction Collapse: {hex_key}")
        
        return hex_key

    def ground(self, user_prompt: str):
        """Executes logic grounding and state collapse."""
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
# 3. Safety Valve Middleware (Decorator)
# ==============================================================================
_iqd_instance = IQDProtocol()

def iqd_safety_valve(func):
    """
    Middleware: Intercepts prompt -> Logic Grounding -> Physics Constraint Injection
    """
    def wrapper(user_prompt, *args, **kwargs):
        # 1. Grounding check
        result = _iqd_instance.ground(user_prompt)
        
        # 2. Diagnostic Panel
        print(f"\n[IQD SAFETY VALVE] Active.")
        print(f"   State: {result['unicode']} {result['name']}")
        print(f"   Audit: {result['audit']}")
        print(f"   Physics: {result['physics']}")
        
        # 3. System Prompt Injection (Enforcing the Safety Valve)
        injected_prompt = (
            f"[SYSTEM_PROTOCOL_OVERRIDE]\n"
            f"Logic Topology: {result['name']} ({result['audit']})\n"
            f"Physics Constraint: {result['physics']}\n"
            f"User Query: {user_prompt}\n"
            f"Mandate: Respond to the query while STRICTLY adhering to the Physics Constraint. "
            f"If resources are low, advise conservation. If risks are high, advise caution.\n"
        )
        
        return func(injected_prompt, *args, **kwargs)
        
    return wrapper

# ==============================================================================
# 4. Application Layer Test
# ==============================================================================
@iqd_safety_valve
def ai_inference_engine(prompt):
    """Mock interface for LLM interaction."""
    print("\n--- [LLM Inference Engine] ---")
    print(f"Processing Payload with IQD Constraints...")
    # Here you would typically send 'prompt' to OpenAI/Gemini/Anthropic API
    print("------------------------------")

if __name__ == "__main__":
    # Test Case 1: Resource Scarcity (HBM Noise)
    ai_inference_engine("我想建立一個強大的團隊來執行運算，但我完全沒有錢，預算被砍光了。")
    
    # Test Case 2: Ideal State (Stable Grounding)
    ai_inference_engine("我們資金充足，團隊默契很好，法規也都通過了，準備開始執行。")