<template>
    <footer class="footer"
            :class="{[`footer-${type}`]: type}"
            :data-background-color="backgroundColor">
        <div class="container">
            <nav>
                <ul>
                    <li>
                        <a href="http://www.wisconsinrobotics.org">
                            Wisconsin Robotics
                        </a>
                    </li>
                    <li>
                        <a href="http://www.wisconsinrobotics.org/about-us.html">
                            About Us
                        </a>
                    </li>
                    <li>
                        <a href="https://github.com/WisconsinRobotics">
                            GitHub
                        </a>
                    </li> 
                </ul>
            </nav>
        </div>
    </footer>
</template>
<script>
export default {
  props: {
    backgroundColor: String,
    type: String
  }
};
</script>
<style>
</style>
