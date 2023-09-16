<script>
  import Logo from '../../assets/img/logo_white.png';
  import LoginForm from '../../components/organisms/Forms/LoginForm.svelte';
  import Image from '../../components/atoms/Image.svelte';

  export let form;
</script>

<div class='login block-center'>
  <div class='card card-login' style="border-top-right-radius: 0; border-bottom-right-radius: 0;">
    <LoginForm form={form} />
  </div>
  <div class='card card-login card-logo'>
    <Image
      imageSrc={Logo}
      imageAlt="Saline Academie Logo"
      imageWidth=320
      class="block-center login-logo"
    />
  </div>
</div>

<style>
  .login{
    display: flex;
    height: 100vh;
    width: 1200px;
    align-items: center;
  }

  .card-login{
    height: 80vh;
  }

  .card-logo{
    background-color: var(--color-secondary);
    border-top-left-radius: 0;
    border-bottom-left-radius: 0;
  }

  :global(.login-logo){
    margin-top: 50%;
    transform: translateY(-50%);
  }
</style>