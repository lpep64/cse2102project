<template>
  <footer class="site-footer">
    <gray-box>
      <div class="gray-box-content">
        Technology Support:<br>
        Luke.pepin@uconn.edu<br>
        Kevin.sarango@uconn.edu<br>
        Richard.vega@uconn.edu <br>
        <br>
        © 2023 University of Connecticut
      </div>
      <img src="..\assets\UConn_Words.png" class="center-image" style="width: 200px; height: 100px;" />
    </gray-box>
  </footer>
</template>

<style scoped>
  /* Reset default margins and paddings */
  body,
  html {
    margin: 0;
    padding: 0;
  }

  /* Wrapper styles to center content */
  .wrapper {
    display: flex;
    flex-direction: column;
    align-items: left;
  }

  /* Footer styles */
  .site-footer {
    background-color: #000E2F;
    color: #fff;
    padding: 10px;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: left;
  }

  /* Gray box content styles */
  .gray-box-content {
    color: rgb(255, 255, 255);
    font-size: 15px;
    font-weight: bold;
    text-align: left;
    line-height: 25px;
  }

  .gray-box-content img {
    max-width: 150px; /* Set the maximum width for the image */
    max-height: 150px; /* Set the maximum height for the image */
    margin-left: 545px; /* Center the image horizontally */
    display: inline-block; /* Remove any inline spacing */
  }

  .center-image {
    display: block;
    margin: 0 auto; /* Center the image horizontally */
    margin-top: 10px; /* Add some top margin to separate from the gray-box content */
  }

  .right-align {
    margin-left: auto; /* Move the element to the right side */
  }
</style>
