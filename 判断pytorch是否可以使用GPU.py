import torch

print(f"1. PyTorch 版本: {torch.__version__}")
print(f"2. CUDA 是否可用 (基础检测): {torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"3. 显卡数量: {torch.cuda.device_count()}")
    print(f"4. 显卡名称: {torch.cuda.get_device_name(0)}")
    
    # ⚠️ 关键步骤：实际让显卡跑一个简单的张量计算
    try:
        # 创建一个张量并放到 GPU 上
        x = torch.tensor([1.0, 2.0]).cuda()
        # 在 GPU 上做加法
        y = x + x
        # 强制让 GPU 把结果同步回 CPU（如果这里报错，就是真有问题）
        result = y.cpu().numpy()
        print(f"5. 🎉 GPU 运算测试成功! 计算结果: {result}")
    except Exception as e:
        print(f"5. ❌ GPU 运算测试失败! 错误信息: {e}")
else:
    print("❌ CUDA 不可用，请检查驱动或 PyTorch 是否为 GPU 版本。")

