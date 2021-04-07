function sendrequest() {
    let keywords = document.getElementById('input1').value;
    let domain = document.getElementById('input2').value;
    let myContainer = document.getElementById('myData');
    let tagsContainer = document.getElementById('spanTags');
    if (keywords && domain) {
        myContainer.innerHTML = null;
        tagsContainer.innerHTML=null;
        fetch('http://127.0.0.1:5000/search?domain=' + domain + '&keywords=' + keywords)
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                // console.log(data);
                for (let key in data) {
                    if (data.hasOwnProperty(key) && key !== 'anchor_tags') {
                        let div = document.createElement("div");
                        div.innerHTML = '<b>' + key + ': </b>' + data[key];
                        myContainer.appendChild(div);
                    } else if (data.hasOwnProperty(key) && key === 'anchor_tags') {
                        for (let each_url in data[key]) {
                            if (data[key].hasOwnProperty(each_url)) {
                                let div = document.createElement("div");
                                div.innerHTML = data[key][each_url];
                                tagsContainer.appendChild(div);
                            }
                        }
                    }

                }
            })
            .catch(function (err) {
                console.log(err);
            });
    }
}

