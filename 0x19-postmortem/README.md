# Web Stack Monitoring and Outage Postmortem

This repository contains tasks related to web stack monitoring and postmortem processes. These tasks are designed to enhance your skills in diagnosing issues, setting up monitoring, and creating postmortem reports.

## Table of Contents

1. [Introduction](#introduction)
2. [Task 0: My First Postmortem](#task-0-my-first-postmortem)
3. [Task 1: Make People Want to Read Your Postmortem](#task-1-make-people-want-to-read-your-postmortem)

## Introduction

In the world of software engineering, failures are inevitable. Outages can occur due to various factors, such as bugs, hardware failures, traffic spikes, and more. Postmortems are valuable tools used to document and learn from these failures, helping to understand their causes, impacts, and preventive measures.

This repository includes tasks that simulate scenarios involving web stack issues and outages. By completing these tasks, you will practice diagnosing problems, setting up monitoring systems, and writing effective postmortem reports.

## Task 0: My First Postmortem

### Scenario: Database Connection Outage

**Issue Summary:**
- **Duration:** 2 hours (10:00 AM - 12:00 PM UTC)
- **Impact:** Users experienced slow response times and intermittent errors when accessing the application.
- **Root Cause:** The database server exhausted its connection pool due to a sudden increase in traffic, causing new connection requests to fail.
  
**Timeline:**
- **10:00 AM:** DevOps team receives alerts about slow response times.
- **10:15 AM:** Engineers investigate and identify the database connection pool exhaustion.
- **10:30 AM:** Misleading assumption made that the issue is related to a recent code deployment.
- **11:00 AM:** Issue escalated to senior DBA and backend lead.
- **11:30 AM:** Investigation reveals the actual cause: connection pool exhaustion due to traffic spike.
- **12:00 PM:** Load balancer settings adjusted to handle increased traffic; database connection pool size increased.

**Root Cause and Resolution:**
- **Root Cause:** The sudden surge in user traffic led to the database connection pool being exhausted.
- **Resolution:** The connection pool size was increased to accommodate higher traffic, and load balancer settings were optimized to distribute traffic evenly.

**Corrective and Preventative Measures:**
- **Improvements:** Implement database connection monitoring; establish automated alerts for connection pool thresholds.
- **Tasks:** Update load balancer configuration; implement database query optimizations to reduce connection usage.

## Task 1: Make People Want to Read Your Postmortem

        Web Users
          |
    ╔═════════════╗
    ║ Load        ║
    ║ Balancer    ║
    ╚═════════════╝
     	   |
      ╔════════╗
      ║ Web    ║
      ║ Server ║
      ╚════════╝
           | 
╔═════════════════════════╗
║          App            ║
╚═════════════════════════╝
           |        
╔═════════════════════════╗
║       Database          ║
╚═════════════════════════╝


Please note that the above scenario and tasks are fictional and are provided for educational purposes. The details provided are for illustrative purposes only.
