"""
AI Queue Tools - AI消息队列工具
支持队列设计、配置、优化
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIQueueTools:
    """
    AI消息队列工具
    支持：设计、配置、优化
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def design_queue_system(self, use_case: str, scale: str) -> Dict:
        """设计队列系统"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为{use_case}设计{scale}规模的消息队列系统：

请返回JSON格式：
{{
    "queue_type": "队列类型",
    "features": ["功能"],
    "tools": ["推荐工具"],
    "architecture": "架构"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"queue": content}

    def generate_rabbitmq_config(self, queues: List[Dict]) -> str:
        """生成RabbitMQ配置"""
        if not self.client:
            return "LLM客户端未配置"

        queues_text = json.dumps(queues, ensure_ascii=False)

        prompt = f"""请生成RabbitMQ配置：

队列：{queues_text}

要求：
1. 队列配置
2. 交换机配置
3. 绑定配置"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_kafka_config(self, topics: List[Dict]) -> str:
        """生成Kafka配置"""
        if not self.client:
            return "LLM客户端未配置"

        topics_text = json.dumps(topics, ensure_ascii=False)

        prompt = f"""请生成Kafka配置：

Topics：{topics_text}

要求：
1. Topic配置
2. 生产者配置
3. 消费者配置"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_celery_config(self, tasks: List[Dict]) -> str:
        """生成Celery配置"""
        if not self.client:
            return "LLM客户端未配置"

        tasks_text = json.dumps(tasks, ensure_ascii=False)

        prompt = f"""请生成Celery配置：

任务：{tasks_text}

要求：
1. Broker配置
2. Result后端
3. 任务路由"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def design_priority_strategy(self, task_types: List[str]) -> Dict:
        """设计优先级策略"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        types_text = ", ".join(task_types)

        prompt = f"""请设计任务优先级策略：

任务类型：{types_text}

请返回JSON格式：
{{
    "priority_levels": [
        {{"level": "优先级", "criteria": "标准"}}
    ],
    "scheduling": "调度策略"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"priority": content}

    def analyze_queue_performance(self, metrics: Dict) -> Dict:
        """分析队列性能"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        metrics_text = json.dumps(metrics, ensure_ascii=False)

        prompt = f"""请分析队列性能：

{metrics_text}

请返回JSON格式：
{{
    "bottlenecks": ["瓶颈"],
    "recommendations": ["建议"],
    "scaling": "扩展建议"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"analysis": content}


def create_tools(**kwargs) -> AIQueueTools:
    """创建队列工具"""
    return AIQueueTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Queue Tools")
    print()

    # 测试
    queue = tools.design_queue_system("订单处理", "中型")
    print(json.dumps(queue, ensure_ascii=False, indent=2))
