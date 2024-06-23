# chatbot/utils.py

import numpy as np
from collections import Counter
from django.contrib.auth import get_user_model

User = get_user_model()

def calculate_similarity(target_user, other_user):
    def is_valid(value):
        return value is not None

    match_count = 0
    total_count = 0

    # 연봉 비교
    if is_valid(target_user.salary) and is_valid(other_user.salary):
        total_count += 1
        if abs(target_user.salary - other_user.salary) <= 5000000:
            match_count += 1

    # 보유 금액 비교
    if is_valid(target_user.money) and is_valid(other_user.money):
        total_count += 1
        if abs(target_user.money - other_user.money) <= 500000:
            match_count += 1

    # 나이 비교
    if is_valid(target_user.age) and is_valid(other_user.age):
        total_count += 1
        if abs(target_user.age - other_user.age) <= 10:
            match_count += 1

    # 성별 비교
    if is_valid(target_user.gender) and is_valid(other_user.gender):
        total_count += 1
        if target_user.gender == other_user.gender:
            match_count += 1

    # 유사도 계산: 일치하는 항목의 비율
    if total_count == 0:
        return 0
    similarity = match_count / total_count
    return similarity

def find_similar_users(target_user):
    similar_users = []

    for user in User.objects.exclude(id=target_user.id):
        similarity = calculate_similarity(target_user, user)
        if similarity > 0.45:  # 유사도가 0보다 큰 경우만 선택
            print(f"Similarity between {target_user.username} and {user.username}: {similarity}")
            similar_users.append((user, similarity))

    return similar_users

def recommend_products(user):
    similar_users = find_similar_users(user)
    product_counter = Counter()
    similar_users_count = len(similar_users)

    for similar_user, similarity in similar_users:
        if similar_user.my_products:
            products = similar_user.my_products.split(',')

            for product in products:
                product = product.strip()
                if product:  # 공백 제거 및 유효한 값만 카운트
                    product_counter[product] += similarity

    if not product_counter:
        return "추천할 상품이 없습니다."

    top_products = product_counter.most_common(5)
    recommended_products = [[product, similarity] for product, similarity in top_products]
    return [recommended_products, similar_users_count]

def get_recommendation(user):
    return recommend_products(user)
