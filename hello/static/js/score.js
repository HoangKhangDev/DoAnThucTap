$(document).ready(function () {
  calc_scores(1);
  calc_scores(2);
  calc_scores(3);

  hide_part(3);
  hide_part(2);
});

function hide_part(part_number) {
  var part = document.querySelectorAll(`.score-part-0${part_number}`);
  part.forEach((element, index) => {
    // if index=0 then hide element td with name header of table
    if (index == 0) {
      element.classList.add("d-none");
    }
    // if index>0 then hide element
    else {
      element.parentElement.classList.add("d-none");
    }
  });
}

function calc_scores(part) {
  var array = document.querySelectorAll(`td .score-part-0${part}`);
  array.forEach((element) => {
    var tach = element.parentElement.parentElement.className.split(" ");
    var max = tach[0];
    var min = tach[1];
    element.addEventListener("change", () => {
      if (element.value != null && element.value.trim().length > 0) {
        if (parseInt(element.value) >= min && parseInt(element.value) <= max) {
          element.classList.remove("is-invalid");
          sum(part);
        } else {
          element.classList.add("is-invalid");
        }
      } else {
        sum(part);
      }
    });
  });
}

function sum(part) {
  var array = document.querySelectorAll(`td .score-part-0${part}`);
  var sum1 = 0;
  var sum2 = 0;
  var sum3 = 0;
  var sum4 = 0;
  var sum5 = 0;

  array.forEach((element) => {
    // score - 1.1 - part - 1;
    // score-1-sum-part-1
    var tach = element.name.split("-");
    if (
      tach[4].includes("one") &&
      tach[3].includes(part) &&
      element.value != null
    ) {
      sum1 += Number(element.value);
    } else if (
      tach[4].includes("two") &&
      tach[3].includes(part) &&
      element.value != null
    ) {
      sum2 += Number(element.value);
    } else if (
      tach[4].includes("three") &&
      tach[3].includes(part) &&
      element.value != null
    ) {
      sum3 += Number(element.value);
    } else if (
      tach[4].includes("four") &&
      tach[3].includes(part) &&
      element.value != null
    ) {
      sum4 += Number(element.value);
    } else if (
      tach[4].includes("five") &&
      tach[3].includes(part) &&
      element.value != null
    ) {
      if (sum5 <= 10) {
        sum5 += Number(element.value);
        element.classList.remove("is-invalid");
      } else {
        element.classList.add("is-invalid");
      }
    }
  });

  if (sum1 > 20) {
    sum1 = 20;
  }
  if (sum2 > 25) {
    sum2 = 25;
  }
  if (sum3 > 20) {
    sum3 = 20;
  }
  if (sum4 > 25) {
    sum4 = 25;
  }

  document.getElementsByName(`score-1-sum-part-${part}-one`)[0].value =
    sum1.toString();
  document.getElementsByName(`score-2-sum-part-${part}-two`)[0].value =
    sum2.toString();
  document.getElementsByName(`score-3-sum-part-${part}-three`)[0].value =
    sum3.toString();
  document.getElementsByName(`score-4-sum-part-${part}-four`)[0].value =
    sum4.toString();
  document.getElementsByName(`score-5-sum-part-${part}-five`)[0].value =
    sum5.toString();

  var sum = sum1 + sum2 + sum3 + sum4 + sum5;
  document.querySelector(`#sum-part-${part}`).innerText = sum.toString();
  if (sum >= 90) {
    document.querySelector(`#classification-part-${part}`).innerText =
      "Xuất Sắc";
  } else if (sum >= 80) {
    document.querySelector(`#classification-part-${part}`).innerText = "Tốt";
  } else if (sum >= 65) {
    document.querySelector(`#classification-part-${part}`).innerText = "Khá";
  } else if (sum >= 50) {
    document.querySelector(`#classification-part-${part}`).innerText =
      "Trung Bình";
  } else if (sum >= 35) {
    document.querySelector(`#classification-part-${part}`).innerText = "Yếu";
  } else {
    document.querySelector(`#classification-part-${part}`).innerText = "Kém";
  }
}

function save_data(part){
  var arr = document.querySelectorAll(`td .score-part-0${part}`);
  var check_error=false;
  var arr_name_error=[]
  arr.forEach((item)=>{
    tach = item.name.split("-");
    if(item.classList.length>2){
      check_error=true;
      arr_name_error.push(tach[1])
    }
  })
  if(check_error==true) {
    var chuoi=''
    arr_name_error.forEach((i)=>{
      chuoi=chuoi+" "+i
    })
    alert(`Kiểm tra lại điểm! Vì có điểm bạn nhập không đúng!!!Xem lại mục (${chuoi})`)
  }

}
