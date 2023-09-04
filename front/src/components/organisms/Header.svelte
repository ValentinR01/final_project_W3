<script>
  import Image from "../atoms/Image.svelte";
  import Logo from '../../assets/img/logo_color.png'
  import Account from "../../assets/img/account.png";
  import Menu from "../molecules/Menu.svelte";

  /**
  * @type {string | undefined}
  */
   export let employeePicture;
   export let currentPage = 'home';
   
</script>

<div class='header'>
  <a href="/">
    <Image
      imageSrc={Logo}
      imageAlt="Saline Academie Logo"
      imageWidth=160
    />
  </a>

  <Menu currentPage={currentPage}/>

  <Image
    imageSrc={employeePicture ? employeePicture : Account }
    imageAlt="Employee picture"
    imageWidth=50
    border
  />
</div>

<style>
  .header{
    display: flex;
    padding: var(--spacing-3) var(--spacing-5);
    align-items: center;
    column-gap: var(--spacing-3);
    background-color: var(--color-background-secondary);
  }
</style>