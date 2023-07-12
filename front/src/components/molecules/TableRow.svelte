<script lang='ts'>
  import Icon from '../atoms/Icon.svelte';
  import ArrowRightIcon from '../../assets/icons/ArrowRightIcon.svelte';
  import CircleIcon from '../../assets/icons/CircleIcon.svelte';

  export let selectedRowElements: any;

  let isTrue : any = []

  for (const selectedRowElement of selectedRowElements) {
    if (Number.isInteger(selectedRowElement.has_high_priority)) {
      isTrue.has_high_priority_is_true = true;
    }
    if (Number.isInteger(selectedRowElement.rush_received)) {
      isTrue.rush_received_is_true = true;
    }
    if (Number.isInteger(selectedRowElement.captation_done)) {
      isTrue.captation_done_is_true = true;
    }
    if (Number.isInteger(selectedRowElement.version)) {
      isTrue.version_is_true = true;
    }
    if (selectedRowElement.title && selectedRowElement.title.length > 40) {
      selectedRowElement.title = `${selectedRowElement.title.substr(0, 40)}...`
      console.log(selectedRowElement.title)
    }
  }
</script>

{#each selectedRowElements as selectedRowElement}
	<tr>
		{#if selectedRowElement.title}
			<td>{selectedRowElement.title}</td>
		{/if}
		{#if isTrue.has_high_priority_is_true}
      {#if selectedRowElement.has_high_priority === 1}
        <td>
          <Icon class="block-center" title="prio" color="var(--blue-base)" width="15" height="15">
            <CircleIcon />
          </Icon>
        </td>
      {:else}
        <td></td>
      {/if}
		{/if}
		{#if selectedRowElement.categorie}
			<td>{selectedRowElement.categorie}</td>
		{/if}
		{#if selectedRowElement.language}
			<td>{selectedRowElement.language}</td>
		{/if}
		{#if selectedRowElement.created_at}
			<td>{selectedRowElement.created_at}</td>
		{/if}
		{#if selectedRowElement.status_by_domain}
			<td>{selectedRowElement.status_by_domain}</td>
		{/if}
		{#if selectedRowElement.published_at}
			<td>{selectedRowElement.published_at}</td>
		{/if}
		{#if selectedRowElement.last_assignment_date}
			<td>{selectedRowElement.last_assignment_date}</td>
		{/if}
		{#if selectedRowElement.name_by_domain}
			<td>{selectedRowElement.name_by_domain}</td>
		{/if}
    	{#if selectedRowElement.name_by_domain.length === 0 }
			<td><a href="">Ajouter</a></td>
		{/if}
		{#if isTrue.rush_received_is_true}
      {#if selectedRowElement.rush_received === 1}
        <td>
          <Icon class="block-center" title="rush" color="var(--green)" width="15" height="15">
            <CircleIcon />
          </Icon>
        </td>
      {:else}
        <td>
          <Icon class="block-center" title="no-rush" color="var(--grey)" width="15" height="15">
            <CircleIcon />
          </Icon>
        </td>
      {/if}
		{/if}
		{#if isTrue.version_is_true }
			<td>V.{selectedRowElement.version}</td>
		{/if}
		{#if isTrue.captation_done_is_true}
      {#if selectedRowElement.captation_done === 1}
        <td>
          <Icon class="block-center" title="captation" color="var(--green)" width="15" height="15">
            <CircleIcon />
          </Icon>
        </td>
      {:else}
        <td>
          <Icon class="block-center" title="no-captation" color="var(--grey)" width="15" height="15">
            <CircleIcon />
          </Icon>
        </td>
      {/if}
		{/if}
    <td> 
      <a href="">
        <Icon title="arrow" color="transparent">
          <ArrowRightIcon />
        </Icon> 
      </a> 
    </td>
	</tr>
{/each}

<style>
  tr {
    white-space: nowrap;
    text-transform: capitalize;
  }
  td {
    border-top: 1px solid var(--grey);
    padding: var(--spacing-3);
    white-space: nowrap;
  }
  tr td:last-child {
    padding: 0;
    vertical-align: middle;
  }
</style>