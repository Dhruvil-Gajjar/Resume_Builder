from datetime import datetime

from django import forms
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory

from core.models import User
from resumes.models import Skills
from resumes.forms import ProfileForm, SkillForm


def manage_profile(request, uid=None):
    context = {}

    SkillInlineForm = inlineformset_factory(User, Skills, form=SkillForm, fk_name='profile', extra=1)

    if uid:
        profile = User.objects.get(pk=uid)
        profile_skills = profile.skills_set.all()

        context.update({
            'profile': profile,
            'profile_skills': profile_skills
        })
    else:
        profile = User()

    form = ProfileForm(instance=profile)

    # Form-Sets
    profile_skill_formset = SkillInlineForm(instance=profile)

    if request.method == "POST":
        form = ProfileForm(request.POST)

        if uid:
            form = ProfileForm(request.POST, instance=profile)

        # Form-Sets
        profile_skill_formset = SkillInlineForm(request.POST, request.FILES)

        if form.is_valid():
            profile_object = form.save(commit=False)

            profile_skill_formset = SkillInlineForm(request.POST, request.FILES, instance=profile_object)

            if not uid:
                profile_object.created_by = request.user

            profile_object.updated_by = request.user
            profile_object.updated_at = datetime.now()

            if profile_skill_formset.is_valid():
                profile_object.save()
                profile_skill_formset.save()

                return redirect('/')
    else:
        if uid:
            form = ProfileForm(instance=profile)
        else:
            form = ProfileForm()
    context.update({
        'form': form,
        'profile_skill_formset': profile_skill_formset,
    })

    return render(request, 'Profiles/profile_management.html', context=context)
