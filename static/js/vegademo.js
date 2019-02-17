function init() {
    var conn = new MapdCon()
        .protocol("https")
        .host("use2-api.mapd.cloud")
        .port("443")
        .dbName("mapd")
        .user("JBE72D0140E8E4D8791A")
        .password("HMRd1eirQJdWm85td82skrATdy1LFBX8duQ9CYxT")
        .connect(function(error, con) {
          con.renderVega(1, JSON.stringify(exampleVega), vegaOptions, function(error, result) {
            console.log(error);
            console.log(result);
            if (error) {
              console.log(error.message);
            }
            else {
              var blobUrl = `data:image/png;base64,${result.image}`
              var body = document.querySelector('body')
              var vegaImg = new Image()
              vegaImg.src = blobUrl
              body.append(vegaImg)
            }
          });
        });
}
