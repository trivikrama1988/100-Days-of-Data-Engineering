# 🏛️ The Senior Data Engineer's Handbook: From Metal to Cloud

[![Work In Progress](https://img.shields.io/badge/Status-Work%20In%20Progress-yellow)](https://github.com/trivikrama1988/100-Days-of-Data-Engineering)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Level](https://img.shields.io/badge/Level-Senior%20%2F%20Architect-red)]()

> **"A Junior Engineer asks: 'How do I write this Spark job?'**
> **A Senior Engineer asks: 'Why is the Catalyst Optimizer failing to prune partitions in this skew scenario?'"**

---

## 🎯 The Pedagogical Philosophy
This is not a syntax guide. This is a **100-day simulation of the cognitive load required of a Senior Data Engineer**.

Most courses teach you tools (Spark, Kafka, Airflow) in isolation. This roadmap teaches you **Architectural Intuition**. We start with "The Metal" (Linux Kernel, Disk I/O, Memory Management) and strictly evolve into "The Cloud" (Distributed Systems, Serverless, and Multi-Cloud Architectures).

**The Goal:** To transition you from a competent technologist to an Architect who understands the cost, performance, and failure modes of every abstraction layer.

---

## 🗺️ The 100-Day Architecture

The curriculum operates on a strict **10-day sprint cadence**.

### [Phase 1: The Metal (Days 1–20)](phase-1-the-metal/)
**Focus:** Operating Systems, Database Internals, and the Physics of I/O.
* **Why:** If you don't understand the Linux Page Cache, you can't debug a Spark Spill. If you don't understand the Oracle WAL, you can't understand the HDFS Edit Log.
* **Key Topics:** Linux Kernel, Inodes, ACID, WAL, MVCC, OLAP vs OLTP Storage.

### [Phase 2: The Distributed Foundation (Days 21–40)](phase-2-distributed/)
**Focus:** The Network, Scalability, and the "Shuffle."
* **Why:** Learning to survive hardware failure. Understanding that "Network is unreliable" is a feature, not a bug.
* **Key Topics:** HDFS, MapReduce Internals, YARN Schedulers, HBase (LSM Trees), Kafka Protocol.

### [Phase 3: Spark Mastery (Days 41–60)](phase-3-spark/)
**Focus:** In-Memory Processing, Optimization, and Internals.
* **Why:** Moving beyond the DataFrame API to understand the Catalyst Optimizer and Project Tungsten.
* **Key Topics:** RDDs, DAGs, Shuffle Sort, Memory Management, Structured Streaming, Delta Lake.

### [Phase 4: Cloud Modernization (Days 61–80)](phase-4-cloud/)
**Focus:** Multi-Cloud Architectures (AWS vs GCP vs Azure).
* **Why:** A Senior Engineer must choose the right tool for the job. We compare Redshift, BigQuery, and Snowflake at an architectural level.
* **Key Topics:** Decoupled Storage/Compute, Micro-partitions, Serverless, FinOps.

### [Phase 5: Production Engineering (Days 81–100)](phase-5-production/)
**Focus:** Reliability, DevOps, and System Design.
* **Why:** Code that works on a laptop is a prototype. Code that survives a region outage is Engineering.
* **Key Topics:** Airflow, Kubernetes, Docker, Terraform (IaC), CI/CD, Data Mesh.

---

## 🧪 The "Senior" Exercises
You will not find "Hello World" here. Each day includes a destructive or investigative lab designed to break systems.

* **Day 1:** [The Inode Explosion](phase-1-the-metal/day-01-linux/exercise.md) (Crashing a disk with 0-byte files).
* **Day 12:** [The Hash Spill](phase-1-the-metal/day-12-joins/exercise.md) (Forcing a Join to spill to disk).
* **Day 27:** [The Queue War](phase-2-distributed/day-27-schedulers/exercise.md) (Starving a job using YARN schedulers).
* **Day 88:** [The State Lock](phase-5-production/day-88-terraform/exercise.md) (Breaking Terraform state with concurrent applies).

---

## 🏆 Capstone Projects
Five unique, portfolio-grade projects that solve "Anti-Patterns":

1.  **The LSM Tree DB Engine:** Build a database from scratch (MemTable + SSTable) in Python.
2.  **The ProtoBuf Schema Registry:** Enforce binary compatibility in a CI/CD pipeline.
3.  **The Out-of-Order Time Machine:** Handle 7-day late data using Spark Watermarking and Side-Outputs.
4.  **The Cloud Arbitrage Broker:** A Multi-Cloud compute broker that spots prices on AWS vs GCP.
5.  **The Chaos Monkey Pipeline:** An Airflow Operator that auto-heals infrastructure when Terraform drifts.

6. **The Enterprise CI/CD Pipeline:** * **Scenario:** A developer pushes code to Git. 
    * **Flow:** **Git** webhook triggers **Jenkins**. Jenkins runs unit tests (PyTest) and builds a Docker image. On success, Jenkins triggers an **Airflow DAG** via API. Airflow spins up a **Databricks** cluster to process data from **Azure Blob** and load it into **Snowflake**.

---

## 🛠️ Tech Stack
* **Languages:** Python, SQL, Scala, Bash.
* **CI/CD:** Git (Source), Jenkins (Build/Test), Airflow (Orchestrate).
* **Compute:** Apache Spark, Databricks, AWS EMR, Google Dataflow.
* **Storage:** HDFS, S3/ADLS/GCS, Delta Lake, Snowflake, BigQuery.
* **Orchestration:** Apache Airflow.
* **Infrastructure:** Docker, Kubernetes, Terraform.
* **Streaming:** Apache Kafka.

---

## 🚀 How to Start
1.  **Clone the Repo:** `git clone https://github.com/trivikrama1988/100-Days-of-Data-Engineering.git`
2.  **Start at Phase 1:** Go to `phase-1-the-metal/day-01-linux/`.
3.  **Read the Theory:** Understand the "Why."
4.  **Run the Lab:** Break the system.
5.  **Fix it:** Engineer the solution.

---

*Author: Rakesh Kumar Dash*
*License: MIT*