<script>
  import Link from "../atoms/Link.svelte";

  /**
   * @type {string}
  */
  export let currentPage = 'projects';
  export let role = 'admin';

</script>

<menu class="menu">

  {@html '<!-- Mettre à jour la condition sur les rôles en fonction des entrées en BDD -->'}
  {@html '<!-- Mettre à jour liens après que le routing ait été fait -->'}
  {#if role === 'super admin' || role === 'admin'}
    
  <li >
    <Link
      linkUrl='/dashboard'
      class='text--uppercase {currentPage == 'projects' ? 'link--current' : undefined}'
    > 
      Les projets
    </Link>
  </li>

  <li>
    <Link
      linkUrl='/account'
      class='text--uppercase {currentPage == 'account' ? 'link--current' : undefined}'
    > 
      Vidéos en ligne
    </Link>
  </li>

  {/if}

  {#if role === 'super admin'}
  
  <li>
    <Link
      linkUrl='/dashboard'
      class='text--uppercase {currentPage == 'users' ? 'link--current' : undefined}'
    > 
      Les utilisateurs
    </Link>
  </li>

  {/if}
</menu>

<style>
  .menu{
    width: fit-content;
    display: flex;
    align-items: center;
    column-gap: var(--spacing-4);
  }

  .menu-el--active{
    color: var(--color-primary);
  }
</style>