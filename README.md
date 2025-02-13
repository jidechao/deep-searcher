# 深度搜索器

深度搜索器结合了强大的大语言模型（如DeepSeek、OpenAI等）和向量数据库（如Milvus等），基于私有数据执行搜索、评估和推理，提供高度准确的答案及全面的报告。本项目适用于企业知识管理、智能问答系统以及信息检索场景。

![架构图](./assets/pic/deep-searcher-arch.png)

## 🚀 特性
- **私有数据搜索**：在确保数据安全的同时，最大限度地利用企业内部数据。必要时，可整合在线内容以提供更准确的答案。
- **向量数据库管理**：支持Milvus等向量数据库，允许进行数据分区以实现高效检索。
- **灵活的嵌入选项**：兼容多种嵌入模型，以便进行最优选择。
- **多LLM支持**：支持DeepSeek、OpenAI等大型模型，用于智能问答和内容生成。
- **文档加载器**：支持本地文件加载，网页爬取功能正在开发中。

---

## 🎉 演示
![演示动图](./assets/pic/demo.gif)

## 📖 快速上手
### 安装
使用pip安装深度搜索器：
```bash
# 克隆代码仓库
git clone https://github.com/zilliztech/deep-searcher.git

# 推荐：创建Python虚拟环境
python3 -m venv.venv
source.venv/bin/activate

# 安装依赖
cd deep-searcher 
pip install -e.
```
在环境变量中准备好`OPENAI_API_KEY`。如果在配置中更改了大语言模型，确保准备好相应的API密钥。参考：
- os.environ["FIRECRAWL_API_KEY"] = "fc-**"
- os.environ["OPENAI_API_KEY"] = "9e1e657e-**"
- os.environ["OPENAI_API_BASE"] = "https://api-inference.modelscope.cn/v1/"
- os.environ["JINA_API_TOKEN"] = "jina_**"


### 快速上手演示
```python
from deepsearcher.configuration import Configuration, init_config
from deepsearcher.online_query import query

config = Configuration()

# 在此自定义你的配置，
# 更多配置详情见下方“配置详情”部分。
config.set_provider_config("llm", "OpenAI", {"model": "gpt-4o-mini"})
init_config(config = config)

# 加载本地数据
from deepsearcher.offline_loading import load_from_local_files
load_from_local_files(paths_or_directory=你的本地路径)

# （可选）通过网页爬取加载数据（需要`FIRECRAWL_API_KEY`环境变量）
from deepsearcher.offline_loading import load_from_website
load_from_website(urls=网站网址)

# 查询
result = query("撰写一篇关于xxx的报告。") # 在此处输入你的问题
```
### 配置详情：
#### 大语言模型配置
  <pre><code>config.set_provider_config("llm", "(大语言模型名称)", "(参数字典)")</code></pre>
<p>“大语言模型名称”可以是以下之一：["DeepSeek", "OpenAI", "SiliconFlow", "TogetherAI"]</p>
<p> “参数字典”是一个包含大语言模型类所需参数的字典。</p>

<details>
  <summary>示例（OpenAI）</summary>
    <pre><code>config.set_provider_config("llm", "OpenAI", {"model": "gpt-4o"})</code></pre>
    <p> 关于OpenAI模型的更多详情：https://platform.openai.com/docs/models </p>
</details>

<details>
  <summary>示例（官方DeepSeek）</summary>
    <pre><code>config.set_provider_config("llm", "DeepSeek", {"model": "deepseek-chat"})</code></pre>
    <p> 关于DeepSeek的更多详情：https://api-docs.deepseek.com/ </p>
</details>

<details>
  <summary>示例（SiliconFlow的DeepSeek）</summary>
    <pre><code>config.set_provider_config("llm", "SiliconFlow", {"model": "deepseek-ai/DeepSeek-V3"})</code></pre>
    <p> 关于SiliconFlow的更多详情：https://docs.siliconflow.cn/quickstart </p>
</details>

<details>
  <summary>示例（TogetherAI的DeepSeek）</summary>
    <pre><code>config.set_provider_config("llm", "TogetherAI", {"model": "deepseek-ai/DeepSeek-V3"})</code></pre>
    <p> 关于TogetherAI的更多详情：https://www.together.ai/ </p>
</details>

#### 嵌入模型配置
<pre><code>config.set_embedding_config("embedding", "(嵌入模型名称)", "(参数字典)")</code></pre>
<p>“嵌入模型名称”可以是以下之一：["MilvusEmbedding", "OpenAIEmbedding", "VoyageEmbedding"]</p>
<p> “参数字典”是一个包含嵌入模型类所需参数的字典。</p>

<details>
  <summary>示例（Pymilvus内置嵌入模型）</summary>
    <pre><code>config.set_embedding_config("embedding", "MilvusEmbedding", {"model": "BAAI/bge-base-en-v1.5"})</code></pre>
    <p> 关于Pymilvus的更多详情：https://milvus.io/docs/embeddings.md </p>
</details>

<details>
  <summary>示例（OpenAI嵌入）</summary>
    <pre><code>config.set_embedding_config("embedding", "OpenAIEmbedding", {"model": "text-embedding-3-small"})</code></pre>
    <p> 关于OpenAI模型的更多详情：https://platform.openai.com/docs/guides/embeddings/use-cases </p>
</details>

<details>
  <summary>示例（VoyageAI嵌入）</summary>
    <pre><code>config.set_embedding_config("embedding", "VoyageEmbedding", {"model": "voyage-3"})</code></pre>
    <p> 关于VoyageAI的更多详情：https://docs.voyageai.com/embeddings/ </p>
</details>

### Python命令行界面模式
#### 加载
```shell
deepsearcher --load "你的本地路径或网址"
```
从本地文件加载的示例：
```shell
deepsearcher --load "/path/to/your/local/file.pdf"
```
从网址加载的示例（在环境变量中设置`FIRECRAWL_API_KEY`，更多详情见[FireCrawl](https://docs.firecrawl.dev/introduction)）：
```shell
deepsearcher --load "https://www.wikiwand.com/en/articles/DeepSeek"
```

#### 查询
```shell
deepsearcher --query "撰写一篇关于xxx的报告。"
```

更多帮助信息
```shell
deepsearcher --help
```

---

## 🔧 模块支持
### 🔹 嵌入模型
- [Pymilvus内置嵌入模型](https://milvus.io/docs/embeddings.md)
- [OpenAI](https://platform.openai.com/docs/guides/embeddings/use-cases) （需要`OPENAI_API_KEY`环境变量）
- [VoyageAI](https://docs.voyageai.com/embeddings/) （需要`VOYAGE_API_KEY`环境变量）

### 🔹 大语言模型支持
- [DeepSeek](https://api-docs.deepseek.com/) （需要`DEEPSEEK_API_KEY`环境变量）
- [OpenAI](https://platform.openai.com/docs/models) （需要`OPENAI_API_KEY`环境变量）
- [SiliconFlow](https://docs.siliconflow.cn/en/userguide/introduction) （需要`SILICONFLOW_API_KEY`环境变量）
- [TogetherAI](https://docs.together.ai/docs/introduction) （需要`TOGETHER_API_KEY`环境变量）

### 🔹 文档加载器
- 本地文件
  - PDF（含txt/md）加载器
  - [Unstructured](https://unstructured.io/) （开发中）（需要`UNSTRUCTURED_API_KEY`和`UNSTRUCTURED_URL`环境变量）
- 网页爬虫
  - [FireCrawl](https://docs.firecrawl.dev/introduction) （需要`FIRECRAWL_API_KEY`环境变量）
  - [Jina Reader](https://jina.ai/reader/) （需要`JINA_API_TOKEN`环境变量）
  - [Crawl4AI](https://docs.crawl4ai.com/) （首次使用需运行`crawl4ai-setup`命令）

### 🔹 向量数据库支持
- [Milvus](https://milvus.io/) （与 [Zilliz](https://www.zilliz.com/) 相同）

---

## 📌 未来计划
- 增强网页爬取功能
- 支持更多向量数据库（如FAISS等）
- 增加对更多大型模型的支持
- 提供RESTful API接口

我们欢迎大家贡献代码！给项目加星并分叉，帮助我们打造更强大的深度搜索器！🎯
