<template>
  <section style="position:relative;" class="mb-5 ">
    <img src="@/assets/bank.webp" alt="main_img"
    data-aos="zoom-out" data-aos-duration="600">
    <h1 data-aos="fade-down" data-aos-duration="1500">주변 은행 찾기</h1>
    <h4 data-aos="fade-down" data-aos-duration="1500">원하시는 장소를 선택하고</h4>
    <h4 data-aos="fade-down" data-aos-duration="1500">주변의 은행들을 해보세요 !</h4>
  </section>
    <div class="row container-content mx-auto" id="section">
        <h1 class="fw-bold">✔ &nbsp;&nbsp;주변 은행 찾기</h1>
        <hr style="margin-top: 20px;  margin-bottom: 20px;">
        <div class="my-3 row gy-3">
            <form class="input-group py-0 my-0" @submit.prevent="searchBank">
                <select name="inputProv"
                    v-model="inputProv"
                    @change="inputProvEvent"
                    class="form-select" required
                >
                <option disabled hidden selected value="">
                    도/광역시 선택
                </option>
                <option v-for="prov in store.province" 
                :value="prov">{{ prov }}</option>
                </select>
                                        
                <select name="inputCityEvent"  
                    v-model="inputCity" 
                    @change="inputCityEvent"
                    class="form-select" required
                >
                <option disabled hidden selected value="">
                    시/구 선택
                </option>
                <option v-for="city in store.city[inputProv]"
                    :value="city">{{ city }}</option>
                </select>
                            
                <select name="inputBankEvent"
                    v-model="inputBank"
                    @change="inputBankEvent"
                    class="form-select" required
                    >
                <option disabled hidden selected value="">
                    은행명 선택
                </option>
                <option v-for="bank in store.bankList"
                    :value="bank">{{ bank }}</option>
                </select>
                <button class="btn btn-primary">검색</button>
            </form>
        </div>
        
        <!-- 지도 표시 -->
        <div class="my-3">
            <div id="map"
                style="width:100%; border:1px whitesmoke solid;">
            </div>
        </div>
        <div v-if="isBankDetailVisible">
            <BankDetailComponent v-show="isBankDetailVisible" :bank="selectedBank"/>
        </div>
    </div>
</template>

<script setup>
    import { ref, onMounted } from "vue"
    import { useBankStore } from "@/stores/bank"
    import BankDetailComponent from "@/components/BankDetailComponent.vue";

    const store = useBankStore()
    const inputProv = ref("")
    const inputCity = ref("")
    const inputBank = ref("")
    const map = ref(null)
    const flags = ref([])
    const isBankDetailVisible = ref(false)
    const selectedBank = ref(null)

    const inputProvEvent = (event) => {
        inputProv.value = event.target.value
    }
    const inputCityEvent = (event) => {
        inputCity.value = event.target.value
    }
    const inputBankEvent = (event) => {
        inputBank.value = event.target.value
    }

    let currentInfowindow = null

    const SearchMyBanks = async (data, status) => {
        if (status === kakao.maps.services.Status.OK) {
            resetFlag()
            const bounds = new kakao.maps.LatLngBounds()
            for (let i = 0 ; i < data.length ; i++) {
                setFlag(data[i])
                bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x))
            }
            map.value.setBounds(bounds)
            updateFlag(data)
        } else if(status === kakao.maps.services.Status.ZERO_RESULT) {
            window.alert("검색 결과가 없습니다.")
        }
    }

    function updateFlag(flagss) {
        for (const flag of flagss) {
            flags.value.push({
                marker: null,
                location: flag.place_name,
            })
        }
    }

    const searchResultText = ref("")

    const searchBank = function () {
        const searchAPI = new kakao.maps.services.Places(map.value)
        resetFlag()        
        searchAPI.keywordSearch(
            `${inputProv.value} ${inputCity.value} ${inputBank.value}`,
            (data, status) => {
                if (status === kakao.maps.services.Status.OK) {
                    searchResultText.value = ""
                } else {
                    searchResultText.value = "No result"
                }

                SearchMyBanks(data, status)
            },
            {
                useMapBounds: false,
            }
        )
    }

    const resetFlag = () => {
        for (const flag of flags.value) {
            if (flag.marker) {
                flag.marker.setMap(null)
            }
        }
        flags.value = []
    }

    const setFlag = function (bank) {
        const flag = new kakao.maps.Marker({
            map: map.value,
            position: new kakao.maps.LatLng(bank.y, bank.x),
        })

        flags.value.push({
            flag: flag,
            bank_name: bank.location,
        })

        kakao.maps.event.addListener(flag, "click", function () {
            if (currentInfowindow) {
                currentInfowindow.close()
            }

            const infowindow = new kakao.maps.InfoWindow({
                zIndex: 1,
                content: `<div style="padding:5px;font-size:12px;font-weight:bold;">${bank.place_name}</div>`,
            })
            infowindow.open(map.value, flag)
            currentInfowindow = infowindow

            selectedBank.value = bank
            isBankDetailVisible.value = true
        })
    }

    onMounted( () => {
        const params = {
            // 캠퍼스 기준
            center: new kakao.maps.LatLng(35.2023797, 126.8106778),
            level: 4,
        }
        map.value = new kakao.maps.Map(document.getElementById("map"), params)
    })

</script>

<style scoped>
    #section{
        min-width: 800px;
        max-width: 1200px;        
    }
    #map {
    height:400px;
    }

</style>