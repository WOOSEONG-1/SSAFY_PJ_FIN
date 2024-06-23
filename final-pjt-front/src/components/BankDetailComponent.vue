<template>
    <div class="my-5">
        <h2 class="fw-bold">🚩 &nbsp;&nbsp;{{ bank.place_name }}</h2>
        <hr>
        <table class="table">
            <thead>
                <tr>
                <th scope="col" class="fs-4"></th>
                </tr>
            </thead>
            <tbody class="table-group-divider">
                <tr>
                <th scope="row">상세 주소</th>
                <td class="border-left">{{ bank.address_name }}</td>
                </tr>
                <tr>
                <th scope="row">도로명 주소</th>
                <td>{{ bank.road_address_name }}</td>
                </tr>
                <tr>
                <th scope="row">전화번호</th>
                <td>{{ bank.phone }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup>
    const props = defineProps({'bank' : Object})
</script>

<style scoped>
    th {
        width:200px;
        padding-left:20px;
        font-size: large;
    }
    td {
        font-size:large
    }
</style>