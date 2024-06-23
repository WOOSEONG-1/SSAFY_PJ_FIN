<template>

  <div class="container-content my-5" id="loginbox">
    <h1 class="fw-bold" style="max-width: 1400px;">📖 &nbsp;&nbsp;내 프로필</h1>
    <hr>
    <div class="converter mt-5" v-if="store.profile">
      <div id="board-list" class="mt-2 mb-3">
        <div class="container">
          <table class="board-table">
            <thead>
              <tr class="border-bottom">
                <th scope="col" class="th-num">아이디</th>
                <th scope="col" class="th-title">{{ store.profile.username }}</th>
              </tr>
              <tr class="border-bottom">
                <th scope="col" class="th-num">성별</th>
                <th scope="col" class="th-title" v-if="store.profile.gender === 0">남성</th>
                <th scope="col" class="th-title" v-else>여성</th>
              </tr>
              <tr class="border-bottom">
                <th scope="col" class="th-num">이름</th>
                <th scope="col" class="th-title">{{ store.profile.nickname }}</th>
              </tr>
              <tr class="border-bottom">
                <th scope="col" class="th-num">나이</th>
                <th scope="col" class="th-title">{{ store.profile.age }}</th>
              </tr>
              <tr class="border-bottom">
                <th scope="col" class="th-num">보유 금액</th>
                <th scope="col" class="th-title">{{ store.profile.money }}</th>
              </tr>
              <tr class="border-bottom">
                <th scope="col" class="th-num">Email</th>
                <th scope="col" class="th-title">{{ store.profile.email }}</th>
              </tr>
              <tr class="border-bottom">
                <th scope="col" class="th-num">연봉</th>
                <th scope="col" class="th-title">{{ store.profile.salary }}</th>
              </tr>
            </thead>
          </table>
        </div>
      </div>

      <div class="row justify-content-center">
        <div v-if="store.deposit" class="mt-5 card p-3 text-center" id="chart">
          <h1 class="text-center" style="text-underline-offset: 15px;"><u>가입한 예금 금리 비교</u></h1>
          <div class="d-flex justify-content-center mt-5">
            <canvas id="myChart"></canvas>
          </div>
        </div>

        <div v-if="store.saving" class="mt-5 row text-center card p-3" id="chart">
          <h1 class="text-center" style="text-underline-offset: 15px;"><u>가입한 적금 금리 비교</u></h1>
          <div class="d-flex justify-content-center mt-5">
            <canvas id="myChart2"></canvas>
          </div>
        </div>
      </div>

      <div class="text-end mt-4">
        <RouterLink class="btn btn-success"
          :to="{ name: 'updateProfile', params: { username: store.profile.username } }">
          회원 정보 수정
        </RouterLink>
      </div>
    </div>
  </div>
</template>
<script setup>
import { useUserStore } from '@/stores/user';
import { ref, onMounted } from 'vue';
import { Chart, registerables } from 'chart.js';

// Chart.js 모듈 등록
Chart.register(...registerables);

const store = useUserStore();
const chartDataLoaded = ref(false);
onMounted(() => { })
const loadData = async () => {
  // await store.getProfile(store.username);
  // await store.depositchart(store.username);
  // await store.savingchart(store.username);

  if (store.deposit && store.deposit.deposit_list && store.deposit.deposit_list.length > 0) {
    const deposits = store.deposit.deposit_list;

    const filteredData = deposits.map(deposit => {
      const option = deposit.options.find(option => option.save_trm === 12);
      return {
        name: deposit.fin_prdt_nm,
        intr_rate: option?.intr_rate,
        intr_rate2: option?.intr_rate2
      };
    }).filter(data => data.intr_rate !== undefined && data.intr_rate2 !== undefined);

    if (filteredData.length > 0) {
      const ctx = document.getElementById('myChart').getContext('2d');
      new Chart(ctx, {
        type: 'bar',
        data: {
          labels: filteredData.map(data => data.name),
          datasets: [
            {
              label: '저축 금리',
              data: filteredData.map(data => data.intr_rate),
              backgroundColor: 'skyblue'
            },
            {
              label: '최고 우대 금리',
              data: filteredData.map(data => data.intr_rate2),
              backgroundColor: '#8ED598'
            }
          ]
        },
        options: {
          scales: {
            x: {
              ticks: {
                font: {
                  size: 20,
                  weight: 'bold',
                  color: '#333' // x축 폰트 색상 설정
                }
              }
            },
            y: {
              beginAtZero: true,
              ticks: {
                font: {
                  size: 20,
                  weight: 'bold',
                  color: '#333' // y축 폰트 색상 설정
                }
              }
            }
          },
          plugins: {
            legend: {
              labels: {
                font: {
                  size: 20,
                  weight: 'bold',
                  color: '#333' // 범례 폰트 색상 설정
                }
              }
            }
          }
        }
      });
    } else {
      console.error('No valid data for the chart');
    }
  } else {
    console.error('Deposit list is null, undefined, or empty');
  }

  if (store.saving && store.saving.saving_list && store.saving.saving_list.length > 0) {
    const savings = store.saving.saving_list;

    const filteredData = savings.map(saving => {
      const option = saving.options.find(option => option.save_trm === 12);
      return {
        name: saving.fin_prdt_nm,
        intr_rate: option?.intr_rate,
        intr_rate2: option?.intr_rate2
      };
    }).filter(data => data.intr_rate !== undefined && data.intr_rate2 !== undefined);

    if (filteredData.length > 0) {
      const ctx = document.getElementById('myChart2').getContext('2d');
      new Chart(ctx, {
        type: 'bar',
        data: {
          labels: filteredData.map(data => data.name),
          datasets: [
            {
              label: '저축 금리',
              data: filteredData.map(data => data.intr_rate),
              backgroundColor: 'skyblue'
            },
            {
              label: '최고 우대 금리',
              data: filteredData.map(data => data.intr_rate2),
              backgroundColor: '#8ED598'
            }
          ]
        },
        options: {
          scales: {
            x: {
              ticks: {
                font: {
                  size: 20,
                  weight: 'bold',
                  color: '#333' // x축 폰트 색상 설정
                }
              }
            },
            y: {
              beginAtZero: true,
              ticks: {
                font: {
                  size: 20,
                  weight: 'bold',
                  color: '#333' // y축 폰트 색상 설정
                }
              }
            }
          },
          plugins: {
            legend: {
              labels: {
                font: {
                  size: 20,
                  weight: 'bold',
                  color: '#333' // 범례 폰트 색상 설정
                }
              }
            }
          }
        }
      });
    } else {
      console.error('No valid data for the chart');
    }
  } else {
    console.error('Saving list is null, undefined, or empty');
  }

  chartDataLoaded.value = true;
};

onMounted(() => {
  store.getProfile(store.username);
  store.depositchart(store.username);
  store.savingchart(store.username);
  setTimeout(() => {
    loadData();
      }, 500);
});

</script>

<style scoped>
.converter {
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  padding: 20px;
  padding-left: 50px;
}

.board-table {
  font-size: 15px;
  width: 100%;
  border-top: 1px solid #ccc;
  border-bottom: 1px solid #ccc;
}

/* 게시글 제목 */
.board-table a {
  color: #333;
  display: inline-block;
  line-height: 1.4;
  word-break: break-all;
  vertical-align: middle;
  text-decoration: none;
  font-size: 15px;
}

.board-table a:hover {
  text-decoration: underline;
}

.board-table th {
  text-align: center;
  font-size: 15px;
}

.board-table .th-num {
  width: 100px;
  text-align: center;
  font-size: 20px;
}

.board-table .th-title {
  text-align: center;
  font-size: 20px;
}

.board-table .th-date {
  width: 200px;
  font-size: medium;
}

.board-table th,
.board-table td {
  padding: 14px 0;
}

.board-table tbody td {
  border-top: 1px solid #e7e7e7;
  text-align: center;
}

.board-table tbody th {
  padding-left: 28px;
  padding-right: 14px;
  border-top: 1px solid #e7e7e7;
  text-align: left;
}

.board-table tbody th p {
  display: none;
}

tr:nth-of-type(odd) {
  background-color: whitesmoke;
}

#chart {
  max-width: 1000px;
}
</style>