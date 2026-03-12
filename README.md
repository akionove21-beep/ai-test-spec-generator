# AI Test Specification Generator

Wordの詳細設計書を解析し、
AIを利用してテスト仕様書を自動生成するツール。

## Background

テスト仕様書作成は多くの工数がかかる作業であり、
特に以下の課題がある。

・設計書からテスト観点を抽出する作業
・業務ロジックの理解
・モード別挙動の整理
・期待値の記述

本プロジェクトではAIを利用して
設計書からテストケース生成を支援するツールを開発する。

## Features

・Word詳細設計書解析  
・項目定義抽出  
・AIによるテスト観点生成  
・ルール定義書によるテスト生成  
・Excelテスト仕様書出力  

## Architecture

Word設計書  
↓  
構造解析  
↓  
AI + ルールエンジン  
↓  
テストケース生成  
↓  
Excelテスト仕様書出力  

## Current Progress

STEP1  
Word → design_items.xlsx  

STEP2  
design_items.xlsx → items.json  

STEP3  
AIテストケース生成（開発中）

## Tech Stack

Python  
OpenAI API  
Excel  
Word
